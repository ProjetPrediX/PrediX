from app import login_user, c
import pytest

def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchone()
    if data:
        return True
    else:
        return False

if __name__ == "__main__":
    pytest.main()