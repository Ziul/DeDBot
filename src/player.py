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
