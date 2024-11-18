from asyncio import sleep

from hikari import MessageCreateEvent
from lightbulb import BotApp, Context, Plugin, SlashCommand, add_checks, command, implements

from bot.command_check import check
from bot.sender import send
from gemini.chat import initial_message, next_message, reset_conversation
from persistence import load_source_channels, store_source_channel

all_plugin = Plugin("all_plugin")
source_channels = load_source_channels()


@all_plugin.command()
@add_checks(check)
@command("start", "Start conversation", auto_defer=True)
@implements(SlashCommand)
async def start(context: Context) -> None:
    await _start(await initial_message(), context)


@all_plugin.command()
@add_checks(check)
@command("quiet_start", "Start conversation without notifying other users", ephemeral=True)
@implements(SlashCommand)
async def quiet_start(context: Context) -> None:
    await _start("Replying to all messages.", context)


@all_plugin.command()
@add_checks(check)
@command("stop", "Stops conversation")
@implements(SlashCommand)
async def stop(context: Context) -> None:
    reset_conversation(context.channel_id)
    source_channels.discard(context.channel_id)
    await send("Conversation stopped.", context.respond)


@all_plugin.command()
@add_checks(check)
@command("restart", "Restarts conversation and its context")
@implements(SlashCommand)
async def restart(context: Context) -> None:
    reset_conversation(context.channel_id)
    await send("Conversation restarted", context.respond)


@all_plugin.listener(event=MessageCreateEvent)
async def on_message(event: MessageCreateEvent) -> None:
    if not event.is_human or event.channel_id not in source_channels:
        return
    channel = await event.message.fetch_channel()
    async with channel.trigger_typing():
        await sleep(0.1)  # Give the bot time to trigger typing indicator.
        text = event.message.content
        attachment_urls = map(lambda a: a.url, event.message.attachments)
        response = await next_message(channel.id, text, attachment_urls)
        await send(response, event.message.respond)


async def _start(message: str, context: Context) -> None:
    reset_conversation(context.channel_id)
    source_channels.add(context.channel_id)
    store_source_channel(context.channel_id)
    await send(message, context.respond)


def load(bot: BotApp) -> None:
    bot.add_plugin(all_plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(all_plugin)
