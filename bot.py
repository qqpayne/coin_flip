from telebot import TeleBot
from random import randint
from telebot import types

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
P.S. you can use bot inline; just type @coin_flips_bot in any chat
"""


@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, HELP_TEXT)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, START_TEXT)


def choice() -> str:
    random = randint(0, 1)
    return "Heads" if random == 1 else "Tails"


@bot.message_handler(commands=["coin"])
def flip_coin(message):
    bot.send_message(message.chat.id, choice())


@bot.inline_handler(lambda query: True)
def flip_coin_inline(inline_query):
    r = types.InlineQueryResultArticle(
        id="1",
        title="Flip a coin",
        input_message_content=types.InputTextMessageContent(message_text=choice()),
    )
    bot.answer_inline_query(inline_query.id, [r], cache_time=0, is_personal=True)


def main():
    while True:
        try:
            bot.polling()
        except:
            pass


if __name__ == "__main__":
    main()
