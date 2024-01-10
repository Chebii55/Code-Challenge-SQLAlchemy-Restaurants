from models import Customer,Review,Restaurant
# - `Restaurant reviews()`

#  - returns a collection of all the reviews for the `Restaurant`
def reviews(session,restaurant_id):
    return session.query(Review).filter(Review.restaurant_id == restaurant_id).all()

# - `Restaurant customers()`

#  - returns a collection of all the customers who reviewed the `Restaurant`

def customers(session,restaurant_id):
    revieews=reviews(session,restaurant_id)
    customers=[]
    for i in revieews:
        customers.append(session.query(Customer).filter(Customer.id == i.customer_id).first())
    return customers


# - `Restaurant fanciest(), this method should be a class method`

#  - returns _one_ restaurant instance for the restaurant that has the highest  price
def fanciest(session):
    all_resturant = session.query(Restaurant).all()
    fanciest_restaurant:Restaurant=all_resturant[0]
    for resturant in all_resturant:
         if fanciest_restaurant.price < resturant.price:
             fanciest_restaurant = fanciest_restaurant
    return fanciest_restaurant


# - `Restaurant all_reviews()`

#  - should return an list of strings with all the reviews for this restaurant

#    formatted as follows:

# [

#  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",

#  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",

# ]
def all_reviews(session,restaurant_id):
    output = []
    all_review_r = reviews(session,restaurant_id)
    restaurant_name = session.query(Restaurant).filter(Restaurant.id == restaurant_id).first().name
    for review in all_review_r:
        Customer_name = session.query(Customer).filter(Customer.id == review.customer_id).first().full_name
        output.append(f"Review for {restaurant_name} by {Customer_name}: {review.star_rating} stars.")
                      
    return output

#TEST
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_engine('sqlite:///resturant_reviews.db')
# Session = sessionmaker(bind=engine)
# session = Session()
# print(all_reviews(session,5))