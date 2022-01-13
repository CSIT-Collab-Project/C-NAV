import flask
from flask import Flask
from flask.helpers import send_from_directory
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/login')
def login():
    return send_from_directory('../Frontend', 'login.html')

@app.route('/')
def home():
    return send_from_directory('../Frontend','index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
