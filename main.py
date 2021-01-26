from flask import Flask
from config.config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime as dt
from flask_restplus import Api

app = Flask(__name__)
app.config.from_object(DevConfig)
api = Api(app)


db = SQLAlchemy(app)

from controller.UserProfile import users
app.register_blueprint(users, url_prefix="/users")

#"""

# SWAGGER-UI
SWAGGER_URL = '/api/docs'
API_URL = 'swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
#"""