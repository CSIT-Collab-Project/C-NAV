from pymongo import MongoClient
import subprocess
from Backend.Nodes.Node import Node
from Backend.logger import logger


class Database(object):
    def __init__(self):
        try:
            logger.info('Starting MongoDB executable')
            self.server = subprocess.run('"C:\\Program Files\\MongoDB\\Server\\5.0\\bin\\mongod.exe"', stdout=False)
            logger.info('MongoDB server running')
        except Exception as e:
            logger.error(f'An exception occurred while trying to start the server: {e}')
        else:
            try:
                logger.info('Connecting to the server')
                self.connection = MongoClient()
                logger.info('Server connected')
            except Exception as e:
                logger.error(f'An exception occurred while trying to connect: {e}')
            else:
                try:
                    logger.info('Initialising the database')
                    self.db = self.connection['C-Nav']
                    logger.info('Database initialised')
                except Exception as e:
                    logger.error(f'An exception occurred while trying to initialise the database: {e}')
                else:
                    try:
                        logger.info('Initialising the collection')
                        self.collection = self.db['cache']
                        logger.info('Collection initialised')
                    except Exception as e:
                        logger.error(f'An exception occurred while trying to initialise the collection: {e}')

