from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,Integer,String,ForeignKey,MetaData)
from sqlalchemy.orm import relationship, backref
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)


Base=declarative_base()

class Customer(Base):
    __tablename__='customers'

    id = Column(Integer(), primary_key=True)
    full_name = Column(String())

    reviews=relationship('Review', backref=backref('customers'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'Customer = {self.id} '+ \
                f'name = {self.full_name}'


class Restaurant(Base):
    __tablename__='restaurants'

    id = Column(Integer(), primary_key=True)
    name=Column(String())
    price=Column(Integer())

    reviews=relationship('Review', backref=backref('restaurants'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'Restaurant = {self.id}'+ \
                f'name = {self.name}'+\
                f'price= {self.price}'

class Review(Base):
    __tablename__= 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating=Column(Integer())
    customer_id=Column(Integer(),ForeignKey('customers.id'))
    restaurant_id=Column(Integer(),ForeignKey('restaurants.id'))
    

    def __repr__(self):
        return f'Customer = {self.customer_id} '+ \
                f'Restaurant = {self.restaurant_id}'+ \
                f'rating = {self.star_rating} '