# -*- coding: utf-8 -*-

import os
import logging
import logging.config
from telegram import Updater
from dice import Dice, roll


def start(bot, update, args):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, "Hey!")


def error(bot, update, error):
    logger.critical('Update "%s" caused error "%s"' % (update, error))
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text='Sorry {}, but {}'.format(
        update.first_name, error))


def main():
    global logger
    # load the logging configuration
    real_path = os.path.dirname(os.path.realpath(__file__))
    logging.config.fileConfig(real_path + '/logging.ini')
    logger = logging.getLogger(__name__)

    # Get the dispatcher to register handlers
    updater = Updater(token="TOKEN")
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("roll", Dice.roll)

    # log all errors
    dp.addErrorHandler(error)

    logger.info('Starting new bot')
    roll()
    # Start the Bot
    updater.start_polling()

    # Block until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
