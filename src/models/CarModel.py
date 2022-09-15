from ast import Try
from data.db import get_connection
from .entities.car import Car


class CarModel():
    @classmethod
    def get_cars(self):
        try:
            connection = get_connection()
            cars = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, place, color, model FROM cars ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    car = Car(row[0], row[1], row[2], row[3])
                    cars.append(car.to_JSON())

            connection.close()
            return cars
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_car(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, place, color, model FROM cars WHERE id = %s", (id,))
                row = cursor.fetchone()

                car = None
                if row != None:
                    car = Car(row[0], row[1], row[2], row[3])
                    car = car.to_JSON()

            connection.close()
            return car
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_car(self, car):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO cars (id, place, color, model) 
                                VALUES (%s, %s, %s, %s)""", (car.id, car.place, car.color, car.model))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_car(self, car):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM cars WHERE ID = %s""", (car.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
