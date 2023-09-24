#!/usr/bin/env python3

from faker import Faker

from app import app
from model import db,Restaurant,Pizzas,RestaurantPizza

with app.app_context():
    
    fake = Faker()

    Restaurant.query.delete()

    restaurants = []
    for i in range(25):
        restaurant = Restaurant(
            name = fake.text(max_nb_chars=20),
            address = fake.paragraph(nb_sentences=30),
        )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit()
    

    Pizzas.query.delete()

    pizzas= []
    for i in range(25):
        pizza = Pizzas(
            name = fake.text(max_nb_chars=30),
            ingredient = fake.paragraph(nb_sentences=30),
        )
        pizzas.append(pizza)

    db.session.add_all(pizzas)
    db.session.commit()

    RestaurantPizza.query.delete()

    restaurantpizzas= []
    for i in range(25):
        restaurantpizza = RestaurantPizza(
            price = fake.text(max_nb_chars=30),
            pizza_id = fake.text(max_nb_chars=30),
            restaurant_id = fake.text(max_nb_chars=30),
        )
        restaurantpizzas.append(restaurantpizza)

    db.session.add_all(restaurantpizzas)
    db.session.commit()



