from flask import (
    jsonify, Blueprint, request, send_from_directory
)
import json
# DB methods for interacting with Mongo DB
from f_app.db.models import User, UserPreference

# Utils
from f_app.utils.utils import generate_hash, convert_date_string_to_float

# For Advanced Queries
from mongoengine.queryset.visitor import Q
import mongoengine

# Blue print for main page path. No authentication Views could be done in the time to complete the project
bp = Blueprint('default', __name__, url_prefix='')

@bp.get('/')
@bp.get('/home')
def index():
    # Send static Vue content to front end. Further request made to fetch user data.
    
    return send_from_directory('static', 'index.html')
    # return "Hello world"


@bp.get('/users/getall')
def get_all_users():

    # Error object
    error = None

    users_list = []

    try:    
        # Fetch all users
        users_list = User.objects.only(
            'username',
            'roles',
            'created_at',
            'preferences',
            'active',
        )  
    except Exception as e:
        error = e
    
        
    # Return response depending on operation success
    if error is None:
        
        return (jsonify(users_list), 200)
    else:
        return ("Something went wrong...", 500)


# Create user data
@bp.post('/users/create')
def create_user():
    # Get form data. Match json structure of list in udata.json
    form = request.form
    
        
    if form is None:
        return ("Failed to create user", 400)
    
        
    try:
        # Parse user roles
        roles_list = ['']
        if form["is_user_admin"] == 'true':
            roles_list.append("admin")
        if form["is_user_manager"] == 'true':
            roles_list.append("manager")
        if form["is_user_tester"] =='true':
            roles_list.append("tester")
        
        # Create user preferences
        new_user_preferences = UserPreference(
            timezone = form["user_timezone"]
        )
        
        # Convert created at date string to float
        date_float = convert_date_string_to_float(form["created_at"])
        
        # Validate user preferecne
        try:
            new_user_preferences.validate()
        except Exception as e:
            raise e
         
            
        # Create new user object
        newUser = User(
            username=form["username"],
            password=generate_hash(form["password"]),
            roles=roles_list,
            preferences=new_user_preferences,
            active=form["is_user_active"],
            created_at=date_float
        )
        
        # Validate user data
        try:
            newUser.validate()
        except Exception as e:
            
            raise e
        
        
        # Try saving the user
        try:
            newUser.save()
        except Exception as e:
            raise e
         
        
    except Exception as e:
        return ("Failed to create user", 400)

    return (jsonify({
            "message": "User created successfully",
            "id": newUser.id
        }), 200)

# Delete user data
@bp.delete('/users/<id>/delete')
def delete_user(id):
    
    if id is None:
        return ("Incorrect details", 400)

    try:
        users = User.objects(id=id)
    except Exception as e:
        print(e)
        
    # Check if there are any matches    
    if len(users) == 0:
        return ("Incorrect details", 400)

    # Delete from database
    try:
        users[0].delete()
    except Exception as e:
        return ("Something went wrong...", 500)

    # Check if user still in database
    try:
        users = User.objects(id=id)
    except Exception as e:
        return ("Something went wrong...", 500)
        
    if len(users) == 0:
        return ("User deletion successful", 200)
    else:
        return ("Something went wrong...", 500)

@bp.post('/users/<id>/update')
def update_user(id):
    if id is None:
        return ("Incorrect details", 400)
    
    # Get json object posted
    updated_user_details = request.json
    
    # Loop through the cleaned_user_details and apply updates only for existing keys
    update_data = {}
    # Parse user roles
    roles_list = ['']
        
    for key, value in updated_user_details.items():
        if key == "is_user_admin":
            continue
        elif key == "is_user_manager":
            continue
        elif key == "is_user_tester":
            continue
        elif value is not None:  # Only update if the value is not empty or None
            update_data[f"set__{key}"] = value
    
    if updated_user_details["is_user_admin"]:
        roles_list.append("admin")
    if updated_user_details["is_user_manager"]:
        roles_list.append("manager")
    if updated_user_details["is_user_tester"]:
        roles_list.append("tester")
        
    if len(roles_list) > 1:
        update_data[f'set__roles'] = roles_list
         
    # try to update fields
    try:
        print(update_data)
        User.objects(id=id).update(**update_data)
    except Exception as e:
        return ("Something went wrong...", 500)
    
    users = User.objects(id=id)
    
    print("Hello")
    print(users)
    
    return (jsonify({
        "message": "User update successful",
        "user_details": users[0]
        }), 200)
    
        
    

    

