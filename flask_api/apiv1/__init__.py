from flask import Blueprint
from flask_restful import Api

from author.controllers import AuthorController

VERSION = 1

blueprint = Blueprint('v1', __name__)
api = Api(blueprint)

# Resources
api.add_resource(AuthorController, '/authors/')
