import unittest
from app import login_user, create_usertable, add_userdata

class TestApp(unittest.TestCase):
    def test_login_user(self):
        # Prepare test data
        usernames = ["OKhaled", "SBenlemoudden", "NSebbagh", "FHakkou", "ABahri", "MChakir", "MElmabrouki"]
        passwords = ["Achat1", "Achat2", "SCM1", "SI1", "Magasin1", "Magasin2", "Finance1"]

        # Reset the user table
        create_usertable()

        # Test the login functionality
        for username, password in zip(usernames, passwords):
            result = login_user(username, password)
            if not result:
                add_userdata(username, password)

            self.assertTrue(result, f"Failed to login user: {username}")

if __name__ == "__main__":
    unittest.main()
