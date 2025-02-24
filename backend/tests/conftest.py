import pytest
from f_app import create_app
from f_app.db.db import drop_test_db_collections

@pytest.fixture
def app():
    newApp = create_app({
        "TESTING": True,
        "MONGODB_SETTINGS": {
            "db": "testing",
            "host": "localhost",
            "port": 27017,
            "alias": "default"
        }}
    )
    
    """
        Push app context to app, to push application context.
        Allows access to app globals such as configs and database details.
        
        https://flask.palletsprojects.com/en/stable/appcontext/
        
        Using test_request_context() method is also used to simulate request context
        for example when mocking http requests to the testing application. This gives access
        to the request object inside the application when running tests.
        
        https://flask.palletsprojects.com/en/stable/reqcontext/
    """
    with newApp.app_context():
        yield newApp
    
    with newApp.app_context():
        # Tear down testing db instance
        drop_test_db_collections()
    
@pytest.fixture
def client(app):
    return app.test_client()