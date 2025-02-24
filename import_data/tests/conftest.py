import pytest
from mongoengine import connect
from import_data.src.import_data import import_user_data

# TEST DB CONNECTION CONFIG
test_db_connection_config = {
    "db_name": "testing",
    "db_port": 27017,
    "db_alias": "testing",
    "db_host": "127.0.0.1"
}

@pytest.fixture()
def db():
    
    db = connect(
        test_db_connection_config["db_name"],
        alias=test_db_connection_config["db_alias"],
        port=test_db_connection_config["db_port"],
        host=test_db_connection_config["db_host"]
    )
    
    yield db 
    
    # Teardown db
    db.drop_database('testing')
    
@pytest.fixture()
def data():
    
    user_data = import_user_data(True)
    
    yield user_data
    
    