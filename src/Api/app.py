from flask import Flask,jsonify
from config import config

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()


    