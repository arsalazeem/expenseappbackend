from faker import Faker


class UserFactory:
    def __init__(self):
        self.fake = Faker()

    def create_valid_user_for_signup(self):  # use data model classes build objects later to be implemented
        return {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email": self.fake.email(),
            "password": self.fake.password()
        }

