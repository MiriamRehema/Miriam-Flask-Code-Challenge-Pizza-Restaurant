from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
#from sqlalchemy import CheckConstraint
from sqlalchemy.orm import sessionmaker


db = SQLAlchemy()
class Restaurant(db.Model):
    __tablename__='restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    address=db.column(db.String,unique=True,nullable=False)

    @validates('name',)
    def validate_name(self,unique,name):
        if not name or len(name)<50:
            raise ValueError("Name not found please entre another name")or("Name must be at least 50 characters long.")
            
        return name
    
   

        

    def __repr__(self):
        return f'Restaurant(id={self.id}, name={self.name},address={self.address})'
    


class Pizzas(db.Model):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    ingredient = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())





    def __repr__(self):
        return f'Pizzas(id={self.id}, name={self.name} ,ingredient={self.ingredient})'


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurantpizza'

    restaurant_id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, primary_key=True)
    price= db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates('price',)
    def validate_price(self,unique,price):
        if not 1 <= price <= 30:
            raise ValueError("Price should be  found between 1 and 30")
            
        return price

    def __repr__(self):
        return f'RestaurantPizza(price={self.price}, restaurant_id={self.restaurant_id} pizza_id={self.pizza_id}, )'


