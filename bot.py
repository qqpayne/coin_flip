from telebot import TeleBot
from random import randint

from os import environ


bot = TeleBot(environ["BOT_TOKEN"])

HELP_TEXT = """
Flip a coin. The output will be heads or tails.

Use following commands:
/start - start bot
/help - help text
/coin - flip a coin
"""

START_TEXT = """
A super-modern software development tool that lets you finally decide which framework/tooling/etc to use. By flipping a coin.
"""


@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, HELP_TEXT)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, START_TEXT)


@bot.message_handler(commands=["coin"])
def flip_coin(message):
    random = randint(0, 1)
    text = "Heads" if random == 1 else "Tails"
    bot.send_message(message.chat.id, text)


def main():
    bot.polling()


if __name__ == "__main__":
    main()
