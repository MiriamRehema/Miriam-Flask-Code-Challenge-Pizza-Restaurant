from app import db,app
from model import Restaurant, Pizza, RestaurantPizza


# Create a function to add seed data to the database
with app.app_context():

    db.session.query(Pizza).delete()
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()

    #Create some restaurant records
    restaurant1 = Restaurant(name="Supreme Extravaganza  Pizza", address="758 Main St")
    restaurant2 = Restaurant(name="Spicy   Meat Feast Pizza ", address="456 Opp St")
    restaurant3 = Restaurant(name=" Megga Margherita Pizza", address="675 Atr St")
    restaurant4 = Restaurant(name="Bacon Wrapped  Mushroom Pizza", address="897 Elm St")
    restaurant5 = Restaurant(name="Butter Stuffed Crust BBQ Pizza ", address="245 Noway St")
    restaurant6 = Restaurant(name="Hawaiian Pineapple Teriyaki ", address="9097 Eik St")
    restaurant7= Restaurant(name="Spinach  White Truffle Oil Pizza ", address="618 Jkl St")
    restaurant8 = Restaurant(name="Loaded Baked Pizza crazy", address="092 Ulem St")
    restaurant9 = Restaurant(name="Sweet  Pineapple Pizza ", address="5639 Resm  St")
    restaurant10 = Restaurant(name="Roasted  Tomato Pizza", address="8099 Van St")
    restaurant11 = Restaurant(name="Garlic   Alfredo Pizza ", address="3541 Me  St")
    restaurant12 = Restaurant(name="Triple Chocolate Pizza ", address="9303 Awes St")
    

    db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4,restaurant5, restaurant6,restaurant7, restaurant8,restaurant9, restaurant10,restaurant11, restaurant12,])
    db.session.commit()
                        

    


    # Create some pizza records
    pizza1 = Pizza(name="Pepperoni", ingredient="Pepperoni, cheese, tomato sauce")
    pizza2 = Pizza(name="Margarita", ingredient="Tomato, cheese, basil")
    pizza3 = Pizza(name="BBQ chicken", ingredient="Chicken, cheese")
    pizza4 = Pizza(name="Meat Lovers", ingredient=" beef , tomato sauce")
    pizza5 = Pizza(name="Supreme", ingredient="Tomato, cheese, basil")
    pizza6 = Pizza(name="White pizza", ingredient="Mushrooms, bell peppers")
    pizza7 = Pizza(name="Sausage and mushroom", ingredient="mushroom tomato sauce")
    pizza8 = Pizza(name="Hawaiian", ingredient="Tomato, cheese, basil")
    pizza9 = Pizza(name="Mushroom and olives", ingredient="mushrooms olives")

    db.session.add_all([pizza1, pizza2, pizza3,pizza4, pizza5, pizza6,pizza7, pizza8, pizza9,])
    db.session.commit()



    # Create restaurant-pizza associations with prices
    restaurant_pizza1 = RestaurantPizza(restaurant_id=1, pizza_id=1, price=12)
    restaurant_pizza2 = RestaurantPizza(restaurant_id=1, pizza_id=2, price=14)
    restaurant_pizza3 = RestaurantPizza(restaurant_id=2, pizza_id=2, price=13)
    restaurant_pizza4 = RestaurantPizza(restaurant_id=2, pizza_id=3, price=16)
    restaurant_pizza5 = RestaurantPizza(restaurant_id=3, pizza_id=4, price=19)
    restaurant_pizza6 = RestaurantPizza(restaurant_id=3, pizza_id=5, price=23)
    restaurant_pizza7 = RestaurantPizza(restaurant_id=4, pizza_id=5, price=22)
    restaurant_pizza8 = RestaurantPizza(restaurant_id=4, pizza_id=6, price=29)
    restaurant_pizza9 = RestaurantPizza(restaurant_id=5, pizza_id=7, price=13)
    restaurant_pizza10 = RestaurantPizza(restaurant_id=5, pizza_id=8, price=25)
    restaurant_pizza11 = RestaurantPizza(restaurant_id=6, pizza_id=8, price=27)
    restaurant_pizza12 = RestaurantPizza(restaurant_id=6, pizza_id=9, price=28)

    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4, restaurant_pizza5, restaurant_pizza6, restaurant_pizza7, restaurant_pizza8, restaurant_pizza9, restaurant_pizza10, restaurant_pizza11,restaurant_pizza12])
    db.session.commit()


    

