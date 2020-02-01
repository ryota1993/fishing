#app.py
######  Flask related Libraries   ############
from flask import Flask
from apis import api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

######  Flask&API settings  ############
app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = 'super-secret-fishing'

api.init_app(app)
jwt = JWTManager(app)
cors = CORS(app)

######  Run the app   ###########

if __name__ == "__main__":
    app.run(debug=True)
