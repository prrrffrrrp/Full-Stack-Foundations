from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession= sessionmaker(bind = engine)
session = DBsession()

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print('\n')

UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 9).one()
print(UrbanVeggieBurger.price)

UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()
print(UrbanVeggieBurger.price)
print('='*20)

for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '@2.99'
        session.add(veggieBurger)
        session.commit()

for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print('\n')


