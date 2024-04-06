from flask import Flask
from flask_smorest import Api
from config import initialize_app
from users import users_blueprints
app = Flask(__name__)
initialize_app(app)
api = Api(app)
api.register_blueprint(users_blueprints)
if __name__ == '__main__':
    app.run(port=5000, debug=True)
