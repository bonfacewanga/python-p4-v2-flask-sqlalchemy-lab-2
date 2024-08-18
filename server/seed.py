# server/seed.py

from app import app
from models import db, Customer, Item, Review

with app.app_context():
    db.session.query(Review).delete()
    db.session.query(Item).delete()
    db.session.query(Customer).delete()

    # Add Customers
    customer1 = Customer(name="Tal Yuri")
    customer2 = Customer(name="Sam Smith")
    db.session.add_all([customer1, customer2])

    # Add Items
    item1 = Item(name="Laptop Backpack", price=49.99)
    item2 = Item(name="Insulated Coffee Mug", price=9.99)
    db.session.add_all([item1, item2])

    # Add Reviews
    review1 = Review(comment="Great backpack!", customer=customer1, item=item1)
    review2 = Review(comment="Keeps coffee hot", customer=customer1, item=item2)
    review3 = Review(comment="Not what I expected", customer=customer2, item=item1)
    db.session.add_all([review1, review2, review3])

    # Commit the transaction
    db.session.commit()
