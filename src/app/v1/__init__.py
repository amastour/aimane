from flask import Blueprint
from flask_restx import Api

authorizations = {
    'api_key' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'Authorization',
        "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
    }
}

auth_blueprint = Blueprint('auth_blueprint',__name__)
auth_api = Api(auth_blueprint,
                title="Auth API",
                version="1.0",
                description="Authentication engine",
                security="api_key",
                authorizations=authorizations)

from .views.auth import auth_ns
from .views.user import user_ns
from .views.device import device_ns
from .views.data import data_ns
auth_api.add_namespace(auth_ns)
auth_api.add_namespace(user_ns)
auth_api.add_namespace(device_ns)
auth_api.add_namespace(data_ns)