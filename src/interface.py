#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Python Telegram bot for the Perkins Light Project
"""

from telegram.ext import Updater, CommandHandler
import telegram
import logging
import time
from controller_proxy import *
from color import *
from solid_animation import *
from fade_animation import *
from pong_animation import *
from wipe_animation import *
from splash_animation import *


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

lastSolid = Color("#000000")

controller = Controller('localhost', 8000)

def solid(bot, update, args):

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
    currentTime = time.time()+ .2
    futureTime = currentTime + 1
    start = 0
    end = 1
    animation = SolidAnimation(currentTime, futureTime, start, end,
                               color.get32bit())
    #Send animation to controller
    lastSolid = color
    controller.add_animation(animation)

def fade(bot, update, args):

    #Catch not enough args
    if (len(args) == 0):
        update.message.reply_text('Usage: `/fade <color> [time]`',
                                 parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Construct color
    try:
        color = Color(args[0])
    except:
        update.message.reply_text('Invalid color for `/fade`',
                               parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Init fade time
    fadetime = 1
    if( len(args) >= 2 ):
        try:
            fadetime = float(args[1])
        except:
            update.message.reply_text('Time must be an decimal value for'
                        '`/fade`', parse_mode=telegram.ParseMode.MARKDOWN)
            return

    #Build FadeAnimation
    startColor = lastSolid
    currentTime = time.time()
    futureTime = time.time() + fadetime
    start = 0 #Lets get the whole strip
    end = 1
    animation = FadeAnimation(currentTime, futureTime, start, end,
                               startColor.get32bit(), color.get32bit())
    #Send animation to controller
    lastSolid = color
    controller.add_animation(animation)

def splash(bot, update, args):

    #Catch not enough args
    if (len(args) < 2):
        update.message.reply_text('Usage: `/splash <color> <epoch (0-1)> [time]`',
                                 parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Construct color
    try:
        color = Color(args[0])
    except:
        update.message.reply_text('Invalid color for `/fade`',
                               parse_mode=telegram.ParseMode.MARKDOWN)
        return

    try:
        epoch = float(args[1])
    except:
        #Error message
        return

    #Init fade time
    fadetime = 1
    if( len(args) > 2 ):
        try:
            fadetime = float(args[2])
        except:
            update.message.reply_text('Time must be an decimal value for'
                        '`/fade`', parse_mode=telegram.ParseMode.MARKDOWN)
            return

    #Build splashAnimation
    startColor = lastSolid
    currentTime = time.time()
    futureTime = time.time() + fadetime
    start = 0 #Lets get the whole strip
    end = 1
    animation = SplashAnimation(currentTime, futureTime, start, end, epoch,
                               startColor.get32bit(), color.get32bit())
    #Send animation to controller
    lastSolid = color
    controller.add_animation(animation)

def wipe(bot, update, args):

    #Catch not enough args
    if (len(args) == 0):
        update.message.reply_text('Usage: `/wipe <color> [time]`',
                                 parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Construct color
    try:
        color = Color(args[0])
    except:
        update.message.reply_text('Invalid color for `/wipe`',
                               parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Init fade time
    fadetime = 1
    if( len(args) >= 2 ):
        try:
            fadetime = float(arg[1])
        except:
            update.message.reply_text('Time must be an decimal value for'
                        '`/wipe`', parse_mode=telegram.ParseMode.MARKDOWN)
            return

    #Build WipeAnimation
    startColor = lastSolid
    currentTime = time.time()
    futureTime = time.time() + fadetime
    start = 0 #Lets get the whole strip
    end = 1
    animation = WipeAnimation(currentTime, futureTime, start, end,
                               startColor.get32bit(), color.get32bit())
    #Send animation to controller
    lastSolid = color
    controller.add_animation(animation)


def pong(bot, update, args):

    #Catch not enough args
    if (len(args) == 0):
        update.message.reply_text('Usage: `/pong <color> [time]`',
                                 parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Construct color
    try:
        color = Color(args[0])
    except:
        update.message.reply_text('Invalid color for `/pong`',
                               parse_mode=telegram.ParseMode.MARKDOWN)
        return

    #Init rain time
    fadetime = 10
    if( len(args) > 1 ):
        try:
            fadetime = float(args[1])
        except:
            update.message.reply_text('Time must be an decimal value for'
                        '`/pong`', parse_mode=telegram.ParseMode.MARKDOWN)
            return

    #Build RainbowAnimation
    startColor = lastSolid
    currentTime = time.time()
    futureTime = time.time() + fadetime
    start = 0 #Lets get the whole strip
    end = 1
    animation = PongAnimation(currentTime, futureTime, start, end,
                               startColor.get32bit(), color.get32bit())
    #Send animation to controller
    lastSolid = color
    controller.add_animation(animation)



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
    dp.add_handler(CommandHandler("color", solid, pass_args=True))
    dp.add_handler(CommandHandler("fade", fade, pass_args=True))
    dp.add_handler(CommandHandler("pong", pong, pass_args=True))
    dp.add_handler(CommandHandler("splash", splash, pass_args=True))
    dp.add_handler(CommandHandler("wipe", wipe, pass_args=True))
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
