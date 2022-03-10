from __future__ import absolute_import
from flask import Flask
from flask.helpers import send_from_directory
from backend import main
from Backend.Logger.logger import logger

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/login')
def login():
    logger.info('login')
    return send_from_directory('../Frontend', 'login.html')


@app.route('/')
def home():
    logger.info('home')
    return send_from_directory('../Frontend', 'index.html')


@app.route('/style.css')
def css():
    logger.info('css')
    return send_from_directory('../Frontend', 'style.css')


@app.route('/scripts.js')
def js():
    logger.info('js')
    return send_from_directory('../Frontend', 'scripts.js')


@app.route('/icon-<iconname>')
def icons(iconname):
    logger.info(icons)
    return send_from_directory('../Frontend/icons', iconname + ".png")


@app.route('/directions-<start>-<end>')
async def directions(start, end):
    logger.info('directions')
    directionjson = await main(start, end)
    print(directionjson)
    return directionjson


@app.route('/map<floor>')
def getMap(floor):
    logger.info('getmap')
    return send_from_directory('../Backend', f'map_path{int(floor) - 1}.png')


if __name__ == '__main__':
    logger.info('run')
    app.run(port=8080, debug=True)

