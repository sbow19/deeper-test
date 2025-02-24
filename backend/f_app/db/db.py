from flask_mongoengine import MongoEngine
from flask import  g

# Create MongoEngine once when app initialises
db = MongoEngine()

# Return Mongo CLient connection instance
def init_db():
    return db

# Add db connection context global if no already there, else return db instance
def set_db_globally():
    if 'db' not in g:
        g.db = db

    return g.db

# CLose connection 
def close_db():
    db = g.pop('db')

    if db is not None:
        db.close()

# Drop TEST DB
def drop_test_db_collections():
    # Access the MongoDb connection directly on MongoEngine instance. Run commands on 'default' connection
    # Such as drop database
    db.connection['default'].drop_database('testing')
    return