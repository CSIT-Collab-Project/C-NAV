# 9sP&erx$&M=rY3U*
import pymongo
from pymongo import MongoClient


class Database(object):
    def __init__(self):
        self.uri = 'mongodb+srv://Elias:9sP&erx$&M=rY3U*@cluster0.wlzpp.mongodb.net/C-Nav?retryWrites=true&w=majority'
        self.client = MongoClient(self.uri)
        (self.client['C-Nav'])['Cache']
