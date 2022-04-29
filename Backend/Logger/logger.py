import logging
black = '\u001b[30m'
red = '\u001b[31m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
cyan = '\u001b[36m'
white = '\u001b[37m'
escape = '\u001b[0m'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file = logging.FileHandler('Logs/C-Nav.log')
file.setLevel(logging.DEBUG)
file.setFormatter(logging.Formatter(
    f'%(asctime)s [%(levelname)s] - (%(filename)s) - "%(message)s"', f'%m/%d - %H:%M:%S'))
stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)
stream.setFormatter(logging.Formatter(
    f'{red}[%(levelname)s] {white}-{escape} {magenta}(%(filename)s) {blue}at %(asctime)s {white}- {red}"%(message)s"', f'%H:%M:%S'))
logger.addHandler(file)
logger.addHandler(stream)
