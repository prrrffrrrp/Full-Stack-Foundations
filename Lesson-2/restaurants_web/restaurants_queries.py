from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()


def allRest():
    list_of_restaurants = list()
    allRestaurants = session.query(Restaurant).all()
    for restaurant in allRestaurants:
        list_of_restaurants.append(restaurant.name)
    return list_of_restaurants


def newRest(new_name):
    newRestaurant = Restaurant(name=new_name)
    session.add(newRestaurant)
    session.commit()
