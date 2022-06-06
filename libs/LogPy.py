"""
    Author: Eduardo Zamora
    LogPy v1

"""


class LogPy:

    @staticmethod
    def log(color, message):
        print(LogPy.getColor(color) + message)

    @staticmethod
    def getColor(color):
        if color == 'black':
            return '\033[30m'
        elif color == 'red':
            return '\033[31m'
        elif color == 'green':
            return '\033[32m'
        elif color == 'orange':
            return '\033[33m'
        elif color == 'blue':
            return '\033[34m'
        elif color == 'purple':
            return '\033[35m'
        elif color == 'cyan':
            return '\033[36m'
        elif color == 'lightgrey':
            return '\033[37m'
        elif color == 'darkgrey':
            return '\033[90m'
        elif color == 'lightred':
            return '\033[91m'
        elif color == 'lightgreen':
            return '\033[92m'
        elif color == 'yellow':
            return '\033[93m'
        elif color == 'lightblue':
            return '\033[94m'
        elif color == 'pink':
            return '\033[95m'
        else:
            return '\033[96m'
