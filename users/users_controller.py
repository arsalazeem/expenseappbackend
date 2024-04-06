from flask.views import MethodView
from flask_smorest import Blueprint
from users.users_services import create_new_user, check_if_email_exists
from users.users_schemas import UserSignUpSchema

blp = Blueprint("users", __name__, description="users")


@blp.route("/users/signup")
class UserSignUp(MethodView):

    @blp.arguments(UserSignUpSchema)
    def post(self, user_data):
        email_exists: bool = check_if_email_exists(user_data.get("email"))
        if email_exists:
            return {"msg": "User with this email already exists"}, 409
        response = create_new_user(user_data)
        return response
