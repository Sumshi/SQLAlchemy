#!/usr/bin/python3

# this is connecting file, to connect we use create_engine()
from sqlalchemy import create_engine,text

# create engine object takes in the database url that u are using
engine = create_engine("sqlite:///sample.db",echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello Welcome to ORM"'))

    print(result.all())