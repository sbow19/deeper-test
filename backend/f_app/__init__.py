'''
    Flask application factory
'''
from flask import Flask
import os 
import json

from f_app.db.db import init_db

from f_app.routes import main
from dotenv import load_dotenv

# Config flask server instance
def create_app(test_config_settings=None):
    app = Flask(__name__, static_folder='static')

    # Construct OS path to env file in root
    env_path = os.path.join(os.getcwd(), 'f_app/.env')
    load_dotenv(env_path)
    
    

    # Test settings --> env settings -- default settings
    if test_config_settings is not None:
        app.config.from_mapping(test_config_settings)
    elif os.path.exists(env_path):
        # Get MongoDB settings and parse the dictionary
        mongodb_settings_str = os.getenv('MONGODB_SETTINGS')

        # Parse the string into a dictionary
        if mongodb_settings_str:
            mongodb_settings = json.loads(mongodb_settings_str)
        else:
            mongodb_settings = {}
        app.config.from_mapping(
            MONGODB_SETTINGS = mongodb_settings,
            SECRET_KEY=os.getenv("SECRET_KEY")
        )
    else:
        app.config.from_mapping(
            SECRET_KEY='key',
        )
    


    # GET MONGO ENGINE INSTANCE THEN INITIALIZE CONNECTION
    db = init_db()
    db.init_app(app)
    
    # Register routing blueprints
    app.register_blueprint(main.bp)
    
    return app
    