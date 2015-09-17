from settings import db


class Author(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField()
    email = db.EmailField()
