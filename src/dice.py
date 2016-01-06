# -*- coding: utf-8 -*-

from random import randint
import os
import logging
import logging.config


class Dice(object):
    """docstring for Dice"""
    @classmethod
    def roll(cls, bot, update, args):
        result = []
        chat_id = update.message.chat_id
        logger.info('Message received from ' +
                    update.message.from_user.username)
        if len(args) == 0:
            args = [4, 1]
        elif len(args) == 1:
            args.append(1)
        try:
            for i in range(int(args[1])):
                result.append(randint(1, int(args[0])))
        except MemoryError:
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
    from getpass import getuser
    bot = update = Mock()
    update.message.from_user.username = getuser()
    Dice.roll(bot, update, argv[1:])
