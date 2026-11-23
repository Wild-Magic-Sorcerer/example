#!/usr/bin/env python

from .constants import Constants
import random
import numpy
import matplotlib

class Printer:
    def __init__(self):
        print('Я вызвался!!!')

    @staticmethod
    def print_greeting():
        print(f'Приветствие по умолчанию: {Constants.greetings.value}')

if __name__ == '__main__':
    pass
