from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

try:
    spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
    print(spinach.restaurant.name)
    session.delete(spinach)
    session.commit()
except:
    print('Item is not there. Already deleted')

firstRestaurant = session.query(Restaurant).filter_by(name='First Restaurant')
for i in firstRestaurant:
    print(i.name)

for i in firstRestaurant:
    session.delete(i)
    session.commit()

firstRestaurant = session.query(Restaurant).filter_by(name='First Restaurant')
for i in firstRestaurant:
    print(i.name)


