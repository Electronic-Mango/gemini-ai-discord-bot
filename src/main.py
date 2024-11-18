from os import getenv

from dotenv import load_dotenv
from hikari import Intents
from lightbulb import BotApp


def main():
    load_dotenv()
    intents = Intents.MESSAGE_CONTENT | Intents.DM_MESSAGES | Intents.GUILD_MESSAGES
    bot = BotApp(token=getenv("BOT_TOKEN"), intents=intents, logs="DEBUG")
    bot.load_extensions("bot.commands.all", "bot.commands.ask", "bot.error_handler")
    bot.run()


if __name__ == "__main__":
    main()
