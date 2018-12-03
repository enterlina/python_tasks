import sys
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def info(self, message: str):
        pass

    def debug(self, message: str):
        pass


pass


class SimpleLogger(Logger):
    def info(self, message: str):
        sys.stdout.write('INFO: {}'.format(message))
        pass

    def debug(self, message: str):
        sys.stdout.write('DEBUG: {}'.format(message))
        pass


pass


class PoliteLogger(Logger):

    def info(self, message: str):
        sys.stdout.write('Read this message please: {}'.format(message))
        pass


pass

