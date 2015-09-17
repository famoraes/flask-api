from flask import Flask, Blueprint
from flask_restful import Api, Resource


class AuthorController(Resource):

    def get(self):
        return {'test': 'hello world'}
