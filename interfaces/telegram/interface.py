#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Python Telegram bot for the Perkins Light Project
"""

from telegram.ext import Updater, CommandHandler
import logging
from controller import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def color(bot, update, args):
    color = args[0]
    update.message.reply_text(text='Attempted Color!')
    #Create a color object and pass to handler


def rainbow(bot, update):
    update.message.reply_text('Attempted Rainbow!')

def help(bot, update):
    help_message = (
        'This bot will allow you to control the Perkins Light Project. '
        'I have a set of commands that will allow you to manipulate the PLP.'
        'These should he shown by telegram. However, /color [hex code] is a'
        'great way to start!'
    )
    update.message.reply_text(help_message)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Run bot."""
    updater = Updater("575287013:AAEAGW2cWd0HlUS5QPhBdTsPF4sSbIaJCPU")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("color", color, pass_args=True))
    dp.add_handler(CommandHandler("rainbow", rainbow, pass_args=True))
    dp.add_handler(CommandHandler("help", help))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
