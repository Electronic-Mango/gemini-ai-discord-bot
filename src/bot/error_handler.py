from lightbulb import BotApp, CommandErrorEvent, Plugin

error_handler_plugin = Plugin("error_handler_plugin")


@error_handler_plugin.listener(CommandErrorEvent)
async def on_error(event: CommandErrorEvent) -> None:
    await event.context.respond(str(event.exception))


def load(bot: BotApp) -> None:
    bot.add_plugin(error_handler_plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(error_handler_plugin)
