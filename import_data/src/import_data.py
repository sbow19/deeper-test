
import os
import dotenv
import json

# Mongo Engine library
from mongoengine import connect

# ME Documetn classes
from import_data.src.models import User, UserPreference

# Password Hasing
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# GLOBAL DB OBJECT  
db = None

def generate_hash(string_to_hash):
    return generate_password_hash(string_to_hash)

def convert_date_string_to_float(string_to_float):
    '''
        Markdown guidance indicates that datetime string needs to be dcovnerted into a float.
        Therefore we need to convert the string to datetime object, then convert to a float
    '''
    # Convert string to date time object
    date_obj = datetime.strptime(string_to_float, "%Y-%m-%dT%H:%M:%SZ")

    return date_obj.timestamp()

def ingest_user_data(user_data_list, test_db_client=None):
    
    error = None        
    
    if test_db_client is not None:
        db = test_db_client
        connect("testing")
        
    for user in user_data_list:
        # Parse user roles
        roles_list = ['']
        if user["is_user_admin"]:
            roles_list.append("admin")
        if user["is_user_manager"]:
            roles_list.append("manager")
        if user["is_user_tester"]:
            roles_list.append("tester")
        
        # Create user preferences
        new_user_preferences = UserPreference(
            timezone = user["user_timezone"]
        )
        
        # Convert created at date string to float
        date_float = convert_date_string_to_float(user["created_at"])
        
        # Validate user preferecne
        try:
            new_user_preferences.validate()
        except Exception as e:
            error = e
            break
            
        # Create new user object
        newUser = User(
            username=user["user"],
            password=generate_hash(user["password"]),
            roles=roles_list,
            preferences=new_user_preferences,
            active=user["is_user_active"],
            created_at=date_float
        )
        
        # Validate user data
        try:
            newUser.validate()
        except Exception as e:
            error = e
            break
        
        # try saving the user
        try:
            newUser.save()
        except Exception as e:
            error = e
            break
    
    if error is not None:
        print(error)
        raise error
    

def import_user_data(test=False):
    
    data_path = ''
    
    if  test:
        data_path = os.path.join(os.getcwd(), 'data/udata.json')
    else:
        data_path = os.path.join(os.getcwd(), '..','data/udata.json')
        
    
    user_data_object = {}
    # Read json data
    with open(data_path, 'r') as file:
        user_data_object = json.load(file)
    
    return user_data_object

def fetch_all_users(test_db_client=None):
    
    error = None
    
    try:
        if test_db_client is not None:
            db = test_db_client
            connect("testing")
    except Exception as e:
        error = e
        print(error)
    

    users = User.objects()    
    
    return users

def main(
    testing_config=None
):
    # Load environment variables
    dotenv.load_dotenv()
    
    
    if testing_config is None: 
        try:
            db = connect(
                os.getenv('DB_NAME'),
                host=os.getenv('DB_HOST'),
                port=int(os.getenv('DB_PORT')),
                alias=os.getenv('DB_ALIAS')
            )
            
        
        except Exception as e:
            raise e
    
    elif testing_config:
        try:
            db = connect(
                testing_config('DB_NAME'),
                host=testing_config('DB_HOST'),
                port=testing_config('DB_PORT'),
                alias=testing_config('DB_ALIAS')
            )
            return db
        
        except Exception as e:
            raise e
    
    
    # Import user data
    user_data = None
    try:
        user_data = import_user_data()
    
    except Exception as e:
        raise e

    # Ingest user data by passing in list of users
    error = None
    try:
        ingest_user_data(user_data["users"])
        
    except Exception as e:
        raise e
    
    print("User data ingestion successful")
        
    
        
        
    




if __name__ == '__main__':
    # Run json data import script
    main()
    
    # Disconnect from database on finishing
    if db: 
        db.disconnect()