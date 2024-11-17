from os import getenv

from dotenv import load_dotenv
from hikari import Intents
from lightbulb import BotApp

from bot.commands.all import load as load_all
from bot.commands.ask import load as load_ask
from bot.commands.prompt import load as load_prompt


def main():
    load_dotenv()
    intents = Intents.MESSAGE_CONTENT | Intents.DM_MESSAGES | Intents.GUILD_MESSAGES
    bot = BotApp(token=getenv("BOT_TOKEN"), intents=intents, logs="DEBUG")
    load_all(bot)
    load_ask(bot)
    load_prompt(bot)
    bot.run()


if __name__ == "__main__":
    main()
