from connections import SessionManager
from users.users_model import User
from users.schemas import UserSignUpRes


def create_new_user(current_session, user_data):
    json_data = user_data
    first_name = json_data.get("first_name")
    last_name = json_data.get("last_name")
    email = json_data.get("email")
    password = json_data.get("password")
    session = current_session
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    session.add(new_user)
    session.commit()
    user_schema = UserSignUpRes()
    response_data = user_schema.dump(new_user)  # deserialize new user to return in response
    return {"data": response_data}, 201


def check_if_email_exists(email: str):
    session_manager = SessionManager()
    session = session_manager.create_session()
    users_counts = session.query(User).filter_by(email=email).count()
    session.close()
    if users_counts > 0:
        session.close()
        return True, None
    return False, session
