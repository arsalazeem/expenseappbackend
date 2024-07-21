from flask.views import MethodView
from flask_smorest import Blueprint
from users.users_service import check_if_email_exists, create_new_user
from users.schemas import UserSignUpReq
from utlis import response_handler
from enums import ResponseType
blp = Blueprint("users", __name__, description="users")


@blp.route("/users/signup")
class UserSignUp(MethodView):

    @blp.arguments(UserSignUpReq)
    def post(self, user_data):
        email_exists, session = check_if_email_exists(user_data.get("email"))
        if email_exists:
            return response_handler(msg_type=ResponseType.ERROR.value, status_code=409, description_code=1)
        response = create_new_user(current_session=session, user_data=user_data)
        return response
