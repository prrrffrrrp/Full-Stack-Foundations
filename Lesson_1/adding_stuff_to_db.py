from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession= sessionmaker(bind = engine)
session = DBsession()
firstRestaurant = Restaurant(name = 'First Restaurant')
session.add(firstRestaurant)
session.commit()
firstRestaurant = session.query(Restaurant).first()
print(firstRestaurant.name)

allR = session.query(Restaurant).all()
for r in allR:
    print(r.name)

