import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

# Query all of the puppies and return the result in alphabetical order
all_puppies = session.query(Puppy).order_by(Puppy.name)
all_puppies.all()

# Query all of the puppies that are less than 6 months old organized by the
# youngest first
today = datetime.date.today()
six_months = today - datetime.timedelta(weeks=24)
young_puppies = session.query(Puppy).filter(Puppy.dateOfBirth > six_months)
young_puppies.all()
# Query all the puppies by ascending weight
fat_puppies = session.query(Puppy).order_by(Puppy.weight)

# Tests

for i, puppy in enumerate(all_puppies):
    print(i, puppy.name, puppy.gender, puppy.dateOfBirth, puppy.weight,
          puppy.shelter_id)

print('\n')

for i, puppy in enumerate(young_puppies):
    print(i, puppy.name, puppy.dateOfBirth)

print('\n')

for puppy in fat_puppies:
    print(puppy.name, puppy.weight)

print('\n')


# Query all puppies grouped by the shelter in wich they are staying
# by_shelter = session.query(Puppy).order_by(Puppy.shelter_id)
shelterX = 1
while shelterX <= 5:
    by_shelter = session.query(Puppy).filter_by(shelter_id=shelterX)
    for puppy in by_shelter:
        print(puppy.name, puppy.shelter_id)
    print('\n')
    shelterX += 1

