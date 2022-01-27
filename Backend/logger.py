import logging

FORMAT = logging.Formatter('[%(levelname)s] - (%(filename)s) at %(asctime)s: %(message)s', "%H:%M:%S")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file = logging.FileHandler('database.log')
file.setLevel(logging.DEBUG)
file.setFormatter(FORMAT)
stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)
stream.setFormatter(FORMAT)
logger.addHandler(file)
logger.addHandler(stream)