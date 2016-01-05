# -*- coding: utf-8 -*-

from random import randint
import os
import logging
import logging.config
from telegram import Updater


class Player(object):
    """docstring for Player"""

    def __init__(self, arg):
        super(Player, self).__init__()
        self.arg = arg


class Master(object):
    """docstring for Master"""

    def __init__(self, arg):
        super(Master, self).__init__()
        self.arg = arg


class Dice(object):
    """docstring for Dice"""
    @classmethod
    def roll(cls, bot, update, args):
        result = []
        chat_id = update.message.chat_id
        if len(args) == 0:
            args = [4, 1]
        elif len(args) == 1:
            args.append(1)
        try:
            for i in range(int(args[1])):
                result.append(randint(1, int(args[0])))
        except MemoryError as e:
            bot.sendMessage(chat_id, "Really?")
            logger.warning('Missing some memory here...' + str(args))
            return 0
        if int(args[1]) < 10:
            logger.debug('Dice Result: ' + str(result) +
                         ' = ' + str(sum(result)))
        else:
            logger.debug('Dice result: ' + str(sum(result)))
        if int(args[1]) < 100:
            bot.sendMessage(chat_id, text='Dice result: ' +
                            str(result) + ' = ' + str(sum(result)))
        else:
            bot.sendMessage(chat_id, text='Dice result: ' + str(sum(result)))
        return sum(result)


def roll():
    global logger
    # load the logging configuration
    real_path = os.path.dirname(os.path.realpath(__file__))
    logging.config.fileConfig(real_path + '/logging.ini')
    logger = logging.getLogger(__name__)
    logger.info('Starting new bot')
    from mock import Mock
    from sys import argv
    bot = update = Mock()
    Dice.roll(bot, update, argv[1:])


def start(bot, update, args):
    pass


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
    logger.info('Starting new bot')

    # Get the dispatcher to register handlers
    updater = Updater(token="TOKEN")
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("roll", Dice.roll)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
