from models import Customer,Review,Restaurant
# - `Review customer()`

#  - should return the `Customer` instance for this review

# - `Review restaurant()`

#  - should return the `Restaurant` instance for this review
# - `Review full_review()`

#  - should return a string formatted as follows:
# Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
def customer(session,id):   
    review = session.query(Review).filter(Review.id == id).first()
    return session.query(Customer).filter(Customer.id == review.customer_id).first()

def restaurant(session,id):
    review=session.query(Review).filter(Review.id == id).first()
    return session.query(Restaurant).filter(Restaurant.id == review.restaurant_id).first()

def  full_review(session,id):
    customer_instance=customer(session,id)
    review = session.query(Review).filter(Review.id == id).first()
    restaurant_instance=restaurant(session,id)

    return f"Review for {restaurant_instance.name} by {customer_instance.full_name}: {review.star_rating} stars"





#TEST
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_engine('sqlite:///resturant_reviews.db')
# Session = sessionmaker(bind=engine)
# session = Session()
# print(full_review(session,5))