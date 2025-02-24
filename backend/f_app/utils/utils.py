# Password Hasing
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

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