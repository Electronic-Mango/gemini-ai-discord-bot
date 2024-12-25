# Simple Gemini AI Discord bot

A simple and unofficial Discord bot wrapping [Gemini AI API](https://ai.google.dev/), build with [`hikari`](https://github.com/hikari-py/hikari) and [`lightbulb`](https://github.com/tandemdude/hikari-lightbulb)!

Bot works on servers for everyone, it will respond to DMs only for bot owner.



## Requirements

This bot was built with `Python 3.12`, [`hikari`](https://github.com/hikari-py/hikari), [`lightbulb`](https://github.com/tandemdude/hikari-lightbulb) and [`generative-ai-python`](https://github.com/google-gemini/generative-ai-python).
Response Markdown is formatted with [`mdformat`](https://github.com/hukkin/mdformat) and split into messages with my own [`simple-markdown-splitter`](https://github.com/Electronic-Mango/simple-markdown-splitter).
Full list of Python requirements is in the `requirements.txt` file, you can use it to install all of them.



## Bot permissions

### Message content

This bot requires **message content privileged gateway intent** to function correctly.
This is required as bot responds to all messages in a given channel.

You can enable this content for the whole bot in [Discord Developer Portal](https://discord.com/developers/applications) and specific bot settings.

Currently, bot won't even start without this privileged intent enabled.


### Sending text messages

Bot also requires **Send Messages** in **Text permissions**, as it responds with regular messages.



## Configuration

Configuration is done through a `.env` file. You can copy example file `.env.example` as `.env` and fill required parameters.

```commandline
cp .env.example .env
```


### Discord bot

Only required parameter is a bot token

```dotenv
BOT_TOKEN='<your secret bot token>'
```


You can optionally configure max send message length, by default length of 2000 is used:

```dotenv
MAX_MESSAGE_LENGTH=<custom max message length>
```

If message send by the bot exceeds this value it's split into multiple messages.
2000 is max message length for Discord bots, thus it's used by default.


You can also optionally specify file in which all target channels for `start` command can be stored:

```dotenv
SOURCES_PERSISTENCE_FILE='<path to basic persistence file>'
```

Bot will store all channel IDs where automatic responding is configured in this file.

**It won't store full message conversation.**
After bot is restarted (if the specified file still exists and wasn't modified) it will keep responding in previously configured channels,
however it won't be able to "pick up" the conversation.


### Gemini AI API

One required parameter is [API key](https://ai.google.dev/gemini-api/docs/api-key).

```dotenv
GEMINI_API_KEY='<your secret API key>'
```

Through `.env` you can also configure other parameters:
* `GEMINI_MODEL` - which [model](https://ai.google.dev/gemini-api/docs/models/gemini) to use (`gemini-1.5-flash` is used by default)
* `GEMINI_SYSTEM_INSTRUCTION` - [system instruction](https://ai.google.dev/gemini-api/docs/system-instructions?lang=python)

```dotenv
GEMINI_MODEL='gemini-1.5-flash-8b'
GEMINI_SYSTEM_INSTRUCTION='You are a helpful assistant.'
```


## Commands

All commands work on servers for everyone and in DMs for bot owner.

* `/start` - start responding to all messages in current channel
* `/quiet_start` - start responding to all messages in current channel without notifying other users
* `/stop` - stop responding to messages
* `/quiet_stop` - stop responding to messages without notifying other users
* `/restart` - reset current conversation and removes all context, other than system message
* `/ask` - ask for specific prompt, can be used in channels which aren't actively monitored
* `ask` - **message command**, can use specified message as prompt



## Running the bot

You can run the bot from the source code directly, or in a Docker container.


### From source code

1. Create a Discord bot
2. Create [Gemini AI API key](https://ai.google.dev/gemini-api/docs/api-key)
3. Install all packages from `requirements.txt`
4. Fill `.env` file
5. Run `main.py` file with Python


### Docker

1. Create a Discord bot
2. Create [Gemini AI API key](https://ai.google.dev/gemini-api/docs/api-key)
3. Fill `.env` file
4. Run `docker compose up -d --build` in terminal

Note that `.env` file is used only for loading environment variables into Docker container through compose.
The file itself isn't added to the container.

When using Docker the bot will automatically store channel IDs for purposes of `start` command in `persistence` file located in project root.



## Disclaimer

This bot is in no way affiliated, associated, authorized, endorsed by, or in any way officially connected with Gemini AI or Google.
This is an independent and unofficial project.
Use at your own risk.
