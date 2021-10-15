###################################################################
#   Dependency Inversion Principle (Принцип инверсии зависимостей).
#
#   Модули верхних уровней не должны зависеть от модулей нижних уровней.
#   Оба типа модулей должны зависеть от абстракций.
#   Абстракции не должны зависеть от деталей.
#   Детали должны зависеть от абстракций.
###################################################################

import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f'{msg}\n')

class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF-8') as f:
            f.write(f'{msg}]n')

class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log(self, message, notifier):
        #notifier - это Класс
        notifier().write(f'{self.prefix} {message}')


if __name__ == '__main__':
    logger = Logger()
    logger.log('Starting', TerminalPrinter)
    logger.log('Ann error', FilePrinter)