import unittest
from users.users_service import create_new_user, check_if_email_exists
from connections.db_connection import SessionManager
from tests.factories.user_factory import UserFactory
from faker import Faker
from sqlalchemy.orm.session import Session as expectedSessionType


class UserSignUp(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.session_manager = SessionManager()
        self.session = self.session_manager.create_session()
        self.user_factory = UserFactory()

    def test_creating_a_new_user_success(self):
        user_to_be_created = self.user_factory.create_valid_user_for_signup()
        response, status_code = create_new_user(self.session, user_to_be_created)

        self.assertEqual(201, status_code)
        created_user_data = response["data"]
        self.assertEqual(created_user_data["first_name"], user_to_be_created["first_name"])
        self.assertEqual(created_user_data["last_name"], user_to_be_created["last_name"])
        self.assertEqual(created_user_data["email"], user_to_be_created["email"])

    def test_if_email_already_exists_when_email_present(self):
        # create a new user
        user_to_be_created = self.user_factory.create_valid_user_for_signup()
        response, status_code = create_new_user(self.session, user_to_be_created)

        self.assertEqual(201, status_code)
        # pass the email from already created user in if_email_already_exists method
        user_exists, session = check_if_email_exists(user_to_be_created.get("email"))
        self.assertEqual(user_exists, True)
        self.assertEqual(session, None)

    def test_check_if_email_already_exists_when_email_not_present(self):
        user_exists, session = check_if_email_exists(self.fake.email())
        self.assertEqual(user_exists, False)
        self.assertIsInstance(session, expectedSessionType)

    def tearDown(self):
        if self.session is not None:
            self.session.close()


if __name__ == '__main__':
    unittest.main()
