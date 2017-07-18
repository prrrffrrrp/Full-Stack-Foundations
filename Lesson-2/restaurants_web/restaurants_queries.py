from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant
from sqlalchemy import desc

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()


def allRest():
    list_of_restaurants = list()
    allRestaurants = session.query(Restaurant).order_by(desc(Restaurant.id)).all()
    for restaurant in allRestaurants:
        list_of_restaurants.append(restaurant.name)
    return list_of_restaurants


def newRest(new_rest):
    newRestaurant = Restaurant(name=new_rest)
    session.add(newRestaurant)
    session.commit()


def renameRest(rest_id, new_name):
    editRestaurant = session.query(Restaurant).filter_by(id=rest_id).one()
    editRestaurant.name = new_name
    session.add(editRestaurant)
    session.commit()


def restId(rest_name):
    restaurantId = session.query(Restaurant.id).filter_by(name=rest_name).first()
    return restaurantId[0]

def deleteRest(rest_id):
    pass

#rst_ids = session.query(Restaurant).all()
#for rst in rst_ids:
#    print(rst.name, rst.id)

