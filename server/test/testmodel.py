import pytest
from app import db, Restaurant, Pizza, RestaurantPizza

# Initialize the app (modify this according to your actual setup)
from app import app
app =app()
app.app_context().push()

# Test creating a pizza
def test_create_pizza():
    pizza = Pizza(name='Margherita', ingredient='Tomato, Mozzarella, Basil')
    db.session.add(pizza)
    db.session.commit()

    saved_pizza = Pizza.query.filter_by(name='Margherita').first()
    assert saved_pizza.name == 'Margherita'
