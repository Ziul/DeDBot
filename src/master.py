# -*- coding: utf-8 -*-

from random import randint
import os
import logging
import logging.config
from telegram import Updater



class Master(object):
    """docstring for Master"""

    def __init__(self, arg):
        super(Master, self).__init__()
        self.arg = arg
