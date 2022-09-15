from flask import Flask,jsonify
from config import config
from routes import car_center


app = Flask(__name__)

def page_not_found(error):
    return '<h1>not found</h1>',404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    #BLueprints
    app.register_blueprint(car_center.main,url_prefix='/api/cars')

    #error handler
    app.register_error_handler(404,page_not_found)
    app.run()


    