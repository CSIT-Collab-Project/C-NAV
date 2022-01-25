from pymongo import MongoClient
import subprocess
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file = logging.FileHandler('database.log')
file_format = logging.Formatter('%(asctime)s : %(funcName)s : %(message)s')
file.setLevel(logging.DEBUG)
file.setFormatter(file_format)
stream = logging.StreamHandler()
stream_format = logging.Formatter('%(asctime)s : %(funcName)s : %(message)s')
stream.setLevel(logging.DEBUG)
stream.setFormatter(stream_format)
logger.addHandler(file)
logger.addHandler(stream)


class Database(object):
    def __init__(self):
        logger.info('Starting up database')
        subprocess.run('"C:\\Program Files\\MongoDB\\Server\\5.0\\bin\\mongod.exe"', stdout=False)
        logger.info('Initialising connection')
        self.connection = MongoClient()
        self.db = (self.connection['C-Nav'])['cache']

