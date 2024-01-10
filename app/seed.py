#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Review, Customer
if __name__ == '__main__':
    engine = create_engine('sqlite:///resturant_reviews.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Review).delete()
    session.query(Customer).delete()

    fake = Faker()

    
    restaurant_names = [
        'Tasty Bites Cafe',
        'Gourmet Delights',
        'Sizzling Spice Kitchen',
        'Urban Eats Grill',
        'Mango Tango Bistro',
        'Pasta Paradise',
        'Chopsticks & Noodles',
        'The Green Fork Garden',
        'Ocean Blue Seafood Shack',
        'Fire & Ice Grillhouse',
        'Golden Harvest Diner',
        'Sunny Side Brunch Bar',
        'Moonlight Sweets Bakery',
        'Spicy Fusion Street Food',
        'Rustic Roots Pub',
        'Wholesome Grains Cafe',
        'Wok & Roll Express',
        'Vintage Vineyards Bistro',
        'Flavors of India',
        'Mystic Mushroom Pizzeria',
        # Add more restaurant names as needed
    ]
            
    restaurants = []
    for i in restaurant_names:
        restaurant = Restaurant(
            name =i,
            price= random.randint(1000,10000)
        )

        # add and commit individually to get IDs back
        session.add(restaurant)
        session.commit()

        restaurants.append(restaurant)

    
    for i in range(50):
        customer = Customer(
            full_name =fake.name(),
        )
        # add and commit individually to get IDs back
        session.add(customer)
        session.commit()
        for k in range(random.randint(0, 5)):
            review = Review (
                   star_rating=random.randint(1, 5),
                   customer_id= customer.id,
                   restaurant_id=restaurants[random.randint(0, (len(restaurants)-1))].id
            )
            session.add(review)
            session.commit()
        

    session.commit()
    session.close()
