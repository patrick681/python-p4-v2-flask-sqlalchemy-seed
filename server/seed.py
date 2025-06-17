#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    # Create and initialize a Faker generator
    fake = Faker()

    # Clear all existing data
    Pet.query.delete()

    # Create randomized pet data
    species_list = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    pets = [
        Pet(name=fake.first_name(), species=rc(species_list))
        for _ in range(10)
    ]

    db.session.add_all(pets)
    db.session.commit()