import pytest
from app import login_user, add_userdata, delete_user

def test_login_user():
    # Create a fictitious user
    username = "ss"
    password = "ss"
    add_userdata(username, password)  # Add user to the database

    # Test the login_user function with valid credentials
    result = login_user(username, password)

    # Check if the function returns data (authenticated user)
    assert result is not None

    # Check if the returned username matches the expected username
    assert result[0][0] == username

    # Check if the returned password matches the expected password
    assert result[0][1] == password

    # Remove the fictitious user from the database
    delete_user(username)

