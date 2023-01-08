# Animefy Telegram Bot

The Animefy Telegram Bot is a Python program that allows users to transform their photos into anime-style art using the [deepai anime style transfer model](https://deepai.org/machine-learning-model/fast-style-transfer). The bot can be added to a Telegram group or used in private chats, and it supports images of any size and format.

## Features

- Transform any photo into anime-style art with just a few clicks
- Easy to use and fast processing times
- Supports images of any size and format

## Prerequisites

- Python 3.7 or higher
- The python-telegram-bot library
- A deepai API key

## Installation

1. Clone the repository: `git clone https://github.com/USERNAME/REPOSITORY_NAME.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Create a `config.ini` file in the root directory with the following contents:

`[DEFAULT]`
`api_key = YOUR_API_KEY`
`bot_token = YOUR_BOT_TOKEN`


Replace `YOUR_API_KEY` with your deepai API key, and `YOUR_BOT_TOKEN` with your Telegram bot token.

4. Run the bot: `python bot.py`

## Usage

1. Add the bot to your Telegram group or contacts.
2. Send a photo to the bot.
3. The bot will send back the transformed image.

## Contributions

We welcome contributions to the Animefy Bot! If you have an idea for a new feature or have found a bug, please [open an issue](https://github.com/USERNAME/REPOSITORY_NAME/issues) or [submit a pull request](https://github.com/USERNAME/REPOSITORY
