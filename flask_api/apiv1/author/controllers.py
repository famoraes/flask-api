import json

from flask_restful import Api, Resource
from flask import Flask, Blueprint, request

from .models import Author


class AuthorController(Resource):
    model = Author

    def post(self):
        data = json.loads(request.data)
        author = Author(**data).save()

        return json.loads(author.to_json()), 201

    def get(self, pk=None):
        data = self.model.objects.all().to_json()

        return json.loads(data)

    def put(self, pk):
        return self.patch(pk)

    def patch(self, pk):
        pass
