from flask import Blueprint,jsonify

main=Blueprint('CarCenter_blueprint',__name__)

@main.route('/')
def get_cars():
    return jsonify({'message',"funcionando"})
    