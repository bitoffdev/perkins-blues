#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Python Telegram bot for the Perkins Light Project
"""

from telegram.ext import Updater, CommandHandler
import telegram
import logging
import time
from color import *
from solid_animation import *
from fade_animation import *
from controller import *


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

lastSolid = Color("#000000")

def color(bot, update, args):

    #Catch not enough args
    if (len(args) == 0):
        update.message.reply_text('Usage: `/color <color>`',
                                  parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Construct color
    try:
        color = Color(args[0])
    except:
        update.message.reply_text('Invalid color for `/color`',
                                parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Build SolidAnimation
    currentTime = time.time()
    futureTime = time.time() + 1
    start = 0
    end = 1
    animation = SolidAnimation(currentTime, futureTime, start, end,
                               color.get32bit())
    #Send animation to controller

    update.message.reply_text(text='Attempted Color!')
    lastSolid = color

def color2(bot, update, args):

    #Catch not enough args
    if (len(args) == 0):
        update.message.reply_text('Usage: `/color2 <color> [time]`',
                                 parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Construct color
    try:
        color = Color(args[0])
    except:
        update.message.reply_text('Invalid color for `/color2`',
                               parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Init fade time
    fadetime = 1
    if( len(args) >= 2 ):
        try:
            fadetime = float(arg[1])
        except:
            update.message.reply_text('Time must be an decimal value for'
                        '`/color2`', parse_mode=telegram.ParseMode.MARKDOWN)
            return

    #Build FadeAnimation
    startColor = lastSolid
    currentTime = time.time()
    futureTime = time.time() + fadetime
    start = 0 #Lets get the whole strip
    end = 1
    animation = FadeAnimation(currentTime, futureTime, start, end,
                               startColor.get32bit(), lastColor.get32bit())
    #Send animation to controller
    update.message.reply_text(text='Attempted Color2!')



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
