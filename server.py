from __future__ import absolute_import
import path
import sys
from flask import Flask
from flask.helpers import send_from_directory
from Backend.run import main
from Backend.run import draw_step

sys.path.append(path.Path(__file__).abspath().parent.parent)
from Backend.Logger.logger import logger


def create_app():
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/login')
    def login():
        logger.info('login')
        return send_from_directory('Frontend', 'login.html')

    @app.route('/about')
    def about():
        logger.info('about')
        return send_from_directory('Frontend', 'about.html')

    @app.route('/')
    def home():
        logger.info('home')
        return send_from_directory('Frontend', 'index.html')

    @app.route('/style.css')
    def css():
        logger.info('css')
        return send_from_directory('Frontend', 'style.css')

    @app.route('/scripts.js')
    def js():
        logger.info('js')
        return send_from_directory('Frontend', 'scripts.js')

    @app.route('/icon-<iconname>')
    def icons(iconname):
        logger.info('Icons')
        return send_from_directory('Frontend/Icons', f"{iconname}.png")

    @app.route('/directions-<start>-<end>')
    async def directions(start, end):
        logger.info(f'directions({start}, {end})')
        directionjson = await main(start, end)
        print(directionjson)
        return directionjson

    @app.route('/map<floor>-<step>')
    def getMap(floor, step):
        step = int(step) - 1
        logger.info('getmap')
        return send_from_directory('', f'map_path{int(floor) - 1}-step{step}.png')
        
    return app
