# Read json data
from import_data.src.import_data import import_user_data, ingest_user_data, fetch_all_users

# Test whether connection to database could be established
def test_db_connection(db):
    # Check if there an object received
    assert db is not None


''' 
    Validate whether the recieved data has the shape of the json data
    
    "users": [
    {
      "user": "john_doe_1",
      "password": "9X$mK2pL",
      "is_user_admin": false,
      "is_user_manager": true,
      "is_user_tester": false,
      "user_timezone": "America/New_York",
      "is_user_active": true,
      "created_at": "2023-09-15T08:30:45Z"
    },
    ...
    ]
'''
def test_parse_json_document(data):
    user_data_object = data

    assert user_data_object is not None
    
def test_parse_json_shape(data):
    user_data_object = data

    assert isinstance(user_data_object, dict)
    
    users_list = None
    users_list = user_data_object["users"]
    
    assert isinstance(users_list, list)
    assert len(users_list) > 0
    
    # Check shape of each user object
    expected_structure = {
        "user": str,
      "password": str,
      "is_user_admin": bool,
      "is_user_manager": bool,
      "is_user_tester": bool,
      "user_timezone": str,
      "is_user_active": bool,
      "created_at": str
    }
    
    
    # Check if the user has the right keys
    for user in users_list:
    
        assert user.keys() == expected_structure.keys()
        
        # Check if each key has the correct type
        for key, expected_type in expected_structure.items():
            
            assert isinstance(user[key], expected_type)
    
def test_saved_document_successful(data, db):
    

    assert data is not None
    assert db is not None

    first_three_user_objects = data["users"][0 : 4]
    
    ingest_user_data(first_three_user_objects, db)
    
    # Fetch user data to check
    users = fetch_all_users(db)
    
    print(users)

    
    
    
    