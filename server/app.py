from flask import Flask,request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api,Resource
from model import Restaurant, Pizza, RestaurantPizza
from model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Miriams_Pizza_Restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)



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

class RestaurantList(Resource):

    def get(self):
        restaurants=[]
        for restaurant in Restaurant.query.all():
            restaurant_dict={
                "id":restaurant.id,
                "name":restaurant.name,
                "address":restaurant.address
            }
            restaurants.append(restaurant_dict)
        return make_response(jsonify(restaurants),200)

        
api.add_resource(RestaurantList, '/restaurants')

class RestaurantsByID(Resource):

    def get(self, id):
        restaurant=Restaurant.query.filter_by(id==id).first()
        if restaurant:
            restaurant_dict=restaurant.to_dict()
            return make_response(jsonify(restaurant_dict),200)
        else:
            return make_response(jsonify({"error":"Restaurant not found"}),404)

    
    def delete(self, id):

        restaurant= Restaurant.query.filter(Restaurant.id == id).first()
        if restaurant:
           db.session.delete(restaurant)
           db.session.commit()
           return make_response(jsonify({"message": "Restaurant successfully deleted"}),204)
        else:
            return make_response(jsonify({"error":"Restaurant not found"}),404)

       
    

api.add_resource(RestaurantsByID, '/restaurants/<int:id>')


class PizzaList(Resource):

    def get(self):
        pizzas=[]
        for pizza in Pizza.query.all():
            pizza_dict={
                "id":pizza.id,
                "name":pizza.name,
                "ingredient":pizza.ingredient
            }
            pizzas.append(pizza_dict)
        return make_response(jsonify(pizzas),200)
api.add_resource(PizzaList, '/pizza')


class RestaurantPizza(Resource):
    
    def post(self):
        data = request.get_json()#retrieve json data from the http request body

        # Validate that the required fields are present in the request
        if not all(key in data for key in ("price", "pizza_id", "restaurant_id")):
            return make_response(jsonify({"errors": ["validation errors.include all keys"]}), 400)

       # price = data["price"]
        pizza_id = data["pizza_id"]
        restaurant_id = data["restaurant_id"]

        # Check if the Pizza and Restaurant exist in the database based on their respective ids
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)


        if not pizza or not restaurant:
            return make_response(jsonify({"errors": ["validation errors pizza and restaurant dont exist"]}), 400)

        # Create a new RestaurantPizza
        restaurant_pizza = RestaurantPizza(
            price = data["price"],
            pizza_id = data["pizza_id"],
            restaurant_id = data["restaurant_id"]

        )

        db.session.add(restaurant_pizza)
        db.session.commit()

        # Return data related to the Pizza
        pizza_data = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }

        return make_response(jsonify(pizza_data), 201)
api.add_resource(RestaurantPizza,'/restaurant_pizza')

    
    
   

if __name__ == '__main__':
    app.run(port=5555, debug=True)