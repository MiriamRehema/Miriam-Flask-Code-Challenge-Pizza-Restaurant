#!/usr/bin/env python3

from app import app
from model import db, Restaurant,Pizzas,RestaurantPizza



if __name__ == '__main__':
    
    with app.app_context():
        import ipdb; ipdb.set_trace()