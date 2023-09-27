from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

metadata=MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model,SerializerMixin):
    __tablename__='restaurant'

    serialize_rules=('-pizzas.restaurant','-restaurant.pizza')
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    address=db.Column(db.String,unique=True, nullable=False)

    pizzas=db.relationship('RestaurantPizza',backref='restaurants')

    @validates(name)
    def validate_name(self, key, value):
        if  len(value) >50:
            raise ValueError("Name must be at less than 50 characters long.")
            
        return value
  

class Pizza(db.Model,SerializerMixin):
    __tablename__ = 'pizza'
    serialize_rules=('-restaurant.pizza','-restaurant.pizza')

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    ingredient = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurants=db.relationship('RestaurantPizza',backref='pizza')


class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__ = 'restaurantpizza'
    serialize_rules=('-restaurant','pizza')
    
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    price= db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates(price)
    def validate_price(self, key, value):
        if not 1 <= value <= 30:
            raise ValueError("Price should be  found between 1 and 30")
            
        return value

   
