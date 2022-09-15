from flask import Blueprint,jsonify,request
from models.entities.car import Car

#models 
from models.CarModel import CarModel

main=Blueprint('car_center_blueprint',__name__)

@main.route('/')
def get_cars():
    try:
        cars = CarModel.get_cars()
        return jsonify(cars)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_car(id):
    try:
        car = CarModel.get_car(id)
        if car != None:
            return jsonify(car)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add',methods=['POST'])
def add_car():
    try:
            id = request.json['id']
            place = request.json['place']
            color = request.json['color']
            model = request.json['model']    
            car = Car(id,place,color,model)

            affected_rows = CarModel.add_car(car)

            if affected_rows == 1:
                return jsonify({'message':'se guardo con exito'})
            else:
                return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
   

@main.route('/delete/<id>', methods=['DELETE'])
def delete_car(id):
    try:
        car = Car(id)
        affected_rows   = CarModel.delete_car(car)
        if affected_rows == 1:
            return jsonify({'message': 'borrado con extito'})
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
