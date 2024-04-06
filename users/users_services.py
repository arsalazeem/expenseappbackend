from connections import SessionManager
from users.users_models import User
from users.users_schemas import UserSchema


def create_new_user(user_data):
    json_data = user_data
    first_name = json_data.get("first_name")
    last_name = json_data.get("last_name")
    email = json_data.get("email")
    password = json_data.get("password")
    session_manager = SessionManager()
    session = session_manager.create_session()
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    session.add(new_user)
    user_schema = UserSchema()
    response_data = user_schema.dump(new_user)  # Deserialize new user to return in response
    session.commit()
    session.close()
    return {"data": response_data}, 201


def check_if_email_exists(email: str):
    session_manager = SessionManager()
    session = session_manager.create_session()
    users_counts = session.query(User).filter_by(email=email).count()
    session.close()
    if users_counts > 0:
        return True
    return False
