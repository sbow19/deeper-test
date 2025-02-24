# Check if default routes successful
def test_get_200_on_home(client):
    # Test the `/` endpoint
    response = client.get('/')
    assert response.status_code == 200
    
    # Test the '/home' endpoint
    response = client.get('/')
    assert response.status_code == 200

# Check if saving user data successful
def test_post_user_data_valid(client):
    # Post valid user data to save
    response = client.post('/users/create', data={
        "username": "Sam King",
        "password": "somethingsecret123!",
        "is_user_admin": True,
        "is_user_manager": True,
        "is_user_tester": False,
        "user_timezone": "Africa/Johannesburg",
        "is_user_active": True,
        "created_at": "2023-12-05T11:20:30Z"
    })
    
    # Check that response is 200
    assert response.json["message"] == "User created successfully"
    assert type(response.json["id"]) == str
    assert response.status_code == 200


# Check if saving user data rejected using details
def test_post_user_data_invalid(client):
    # Post valid user data to save
    response = client.post('/users/create', data={
        "username": "Sam King",
        "password": "somethingsecret123!",
    })
    
    # Check that response is 400
    assert response.text == "Failed to create user"
    assert response.status_code == 400
    

# Check that results returns all user details in a list
def test_get_all_user_data(client):
    # Post dummy data
    client.post('/users/create', data={
        "username": "Sam King",
        "password": "somethingsecret123!",
        "is_user_admin": True,
        "is_user_manager": True,
        "is_user_tester": False,
        "user_timezone": "Africa/Johannesburg",
        "is_user_active": True,
        "created_at": "2023-12-05T11:20:30Z"
    })
    
    client.post('/users/create', data={
        "username": "Sam Ki",
        "password": "somethingsecret123!",
        "is_user_admin": True,
        "is_user_manager": True,
        "is_user_tester": False,
        "user_timezone": "Africa/Johannesburg",
        "is_user_active": True,
        "created_at": "2023-12-05T11:20:30Z"
    })
    # Get all data 
    response = client.get('/users/getall')
    
    # Check successful fetch
    assert len(response.json) == 2
    assert response.status_code == 200
    
    # Get Check if Sam Ki details here
    u_found = True
    users = response.json
    for user in users:
        if user["username"] == "Sam Ki" :
            u_found =  True
            break
    assert u_found
    
    # If password returned, then reject
    p_not_found = True
    for user in users:
        if "password" in user:
            p_not_found = False
            break
    assert p_not_found
    
    # If ids not returned, then fail test
    id_found = False
    for user in users:
        if user["_id"] is not None:
            id_found = True
        elif user["_id"] is None:
            id_found = False
            break
    assert id_found
    
    # Check type of id object (must be string)
    first_user = users[0]
    assert type(first_user["_id"]['$oid']) == str

# Check that you can delete user data
def test_delete_user_data(client):
    # Post dummy data
    response = client.post('/users/create', data={
        "username": "Sam King",
        "password": "somethingsecret123!",
        "is_user_admin": True,
        "is_user_manager": True,
        "is_user_tester": False,
        "user_timezone": "Africa/Johannesburg",
        "is_user_active": True,
        "created_at": "2023-12-05T11:20:30Z"
    })
    
    user_id = response.json["id"]
    
    # Delete user
    delete_response = client.delete(f'/users/{user_id}/delete')
    
    # Check for successful status code
    assert delete_response.status_code == 200
    
# Check that you can update a user
def test_update_user_data(client):
    # Post dummy data
    response = client.post('/users/create', data={
        "username": "Sam King",
        "password": "somethingsecret123!",
        "is_user_admin": True,
        "is_user_manager": True,
        "is_user_tester": False,
        "user_timezone": "Africa/Johannesburg",
        "is_user_active": True,
        "created_at": "2023-12-05T11:20:30Z"
    })
    
    user_id = response.json["id"]
    
    # Update data
    update_data = {
        "username": "Jerry Ben",
        "active": False,
        "is_user_admin": False,
        "is_user_manager": False,
        "is_user_tester": True,
    }
    
    # update user (response is new user details)
    update_response = client.post(f'/users/{user_id}/update', json=update_data)
    user_details = update_response.json["user_details"]
    
    # Check for successful status code
    assert update_response.status_code == 200
    assert user_details["username"] == "Jerry Ben"
    assert "tester" in user_details["roles"] 
    assert "manager" not in user_details["roles"]
    assert "admin" not in user_details["roles"] 
    assert not user_details["active"] 
  


    

    