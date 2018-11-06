from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///hollywood.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_christian_bales_roles():
    return session.query(Actor).filter(Actor.name == "Christian Bale").first().roles
    # Return a list of Christian Bale role instances

def return_catwoman_actors():
    return session.query(Role).filter(Role.character == "Catwoman").first().actors
    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors():
    return len(session.query(Role).filter(Role.character == "Batman").first().actors)
    # Return the number of actors that have played Batman
