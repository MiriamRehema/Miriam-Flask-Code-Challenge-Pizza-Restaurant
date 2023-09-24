from flask import Flask,request, make_response
from flask_migrate import Migrate
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Miriams_Pizza_Restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models after initializing SQLAlchemy
from model import Restaurant, Pizzas, RestaurantPizza

api = Api(app)

engine=create_engine('sqlite:///Miriams_Pizza_Restaurant.db')
Session=sessionmaker(bind=engine)

if __name__ == '__main__':
    app.run()


class Home(Resource):
     def get(self):
        
        response_dict = {
            "message": "Welcome to Miriam's Pizza Resataurant",
        }
        
        response = make_response(
            response_dict,
            200
        )

        return response
api.add_resource(Home, '/')

class RestaurantResource(Resource):

    def get(self):

        response_dict_list = [n.to_dict() for n in Restaurant.query.all()]

        response = make_response(
            response_dict_list,
            200,
        )

        return response

api.add_resource(Restaurant, '/restaurant')

class RestaurantsByID(Resource):

    def get(self, id):

        response_dict = Restaurant.query.filter_by(id=id).first().to_dict()

        response = make_response(
            response_dict,
            200,
        )

        return response
    
    def delete(self, id):

        record = Restaurant.query.filter(Restaurant.id == id).first()
        
        db.session.delete(record)
        db.session.commit()

        response_dict = {"message": "record successfully deleted"}

        response = make_response(
            response_dict,
            200
        )

        return response
    

api.add_resource(RestaurantsByID, '/restaurants/<int:id>')


class Pizzas(Resource):

    def get(self):

        response_dict_list = [n.to_dict() for n in Pizzas.query.all()]

        response = make_response(
            response_dict_list,
            200,
        )

        return response
    
api.add_resource(Pizzas, '/pizzas')


class RestaurantPizza(Resource):

    #def get(self):

        #response_dict_list = [n.to_dict() for n in RestaurantPizza.query.all()]

        #response = make_response(
            #response_dict_list,
           # 200,
        #)

       # return response
    
    
    def post(self):
        
        new_record = RestaurantPizza(
            price=request.form['price'],
            pizza_id=request.form['pizza_id'],
            restaurant_id=request.form['restaurant_id'],
        )

        db.session.add(new_record)
        db.session.commit()

        response_dict = new_record.to_dict()

        response = make_response(
            response_dict,
            201,
        )

        return response

api.add_resource(RestaurantPizza, '/restaurant_Pizza')






























































































if __name__ == '__main__':
    app.run(port=5555, debug=True)