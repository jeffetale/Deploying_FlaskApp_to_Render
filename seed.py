from app import *
from models import db, Bird


with app.app_context():

    print('Deleting existing birds...')
    Bird.query.delete()

    print('Creating bird objects...')
    chickadee = Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus')
    grackle = Bird(name='Grackle', species='Quiscalus Quiscula')
    starling = Bird(name='Common Starling', species='Sturnus Vulgaris')
    dove = Bird(name='Mourning Dove', species='Zenaida Macroura')
    chicken = Bird(name='Steaky', species='Pecckis Steckis')
    kiwi = Bird(name='Tangu Nyeusi', species='Black Birdies')

    print('Adding bird objects to transaction...')
    db.session.add_all([chickadee, grackle, starling, dove, chicken, kiwi])

    print('Committing transaction...')
    db.session.commit()

    print('Complete.')
