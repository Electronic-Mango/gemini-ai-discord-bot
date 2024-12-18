from lightbulb import BotApp, Context, Plugin, SlashCommand, add_checks, command, implements, option
from lightbulb.commands import MessageCommand

from bot.command_check import check
from bot.downloader import download_attachments
from bot.sender import send
from gemini.chat import next_message

ask_plugin = Plugin("ask_plugin")


@ask_plugin.command()
@option("query", "Text to ask", str)
@add_checks(check)
@command("ask", "Ask for specific thing", auto_defer=True)
@implements(SlashCommand)
async def ask(context: Context) -> None:
    text = context.options.query
    attachments = await download_attachments(context.attachments)
    response = await next_message(context.channel_id, text, attachments)
    await send(response, context.respond)


@ask_plugin.command()
@add_checks(check)
@command("ask", "Ask for specific thing", auto_defer=True)
@implements(MessageCommand)
async def ask_directly(context: Context) -> None:
    text = context.options.target.content
    attachments = await download_attachments(context.options.target.attachments)
    response = await next_message(context.channel_id, text, attachments)
    await send(response, context.respond)


def load(bot: BotApp) -> None:
    bot.add_plugin(ask_plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(ask_plugin)
