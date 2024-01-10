from models import Customer,Review,Restaurant

def  reviews(session,id):
    return session.query(Review).filter(Review.customer_id == id).all()

def  restaurants(session,id):
    all_reviews = reviews(session,id)
    restaurants=[]
    for review in all_reviews:
        resturant = session.query(Restaurant).filter(Restaurant.id == review.customer_id).first()
        if resturant in restaurants:
            continue
        restaurants.append(resturant)
    return restaurants



def full_name(session, customer_id):
    return session.query(Customer).filter(Customer.id == customer_id).first().full_name


def favorite_restaurant(session, customer_id):
    reviews_by_customer = session.query(Review).filter(Review.customer_id == customer_id).all()
    highest_review:Review = reviews_by_customer[0]
    for re in reviews_by_customer:
        if (highest_review.star_rating < re.star_rating):
            highest_review:Review = re
    return session.query(Restaurant).filter(Restaurant.id == highest_review.restaurant_id).all()[0].name
    
def add_review(session,id,restaurant:Restaurant, rating):
    review = Review (
                   star_rating=rating,
                   customer_id= id,
                   restaurant_id=restaurant.id
            )
    session.add(review)
    session.commit()

def delete_reviews(session,id,restaurant:Restaurant):
    restaurant_selected=session.query(Review).filter(Review.customer_id == id,Review.restaurant_id==restaurant.id).all()
    for review in restaurant_selected:
        session.delete(review)
    session.commit()
    return restaurant_selected



# #TEST
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_engine('sqlite:///resturant_reviews.db')
# Session = sessionmaker(bind=engine)
# session = Session()
# print(full_name(session,7))