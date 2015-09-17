from flask import Flask
from flask.ext.mongoengine import MongoEngine

import apiv1

# Flask App
app = Flask(__name__)

# Settings
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'str89d&#nfdn#&nghd'
app.config['MONGODB_SETTINGS'] = {
    'DB': 'flask_api',
}
app.config['API_PREFIX'] = 'api'

# Set the database
db = MongoEngine(app)

# Blueprints
app.register_blueprint(
    apiv1.blueprint,
    url_prefix='/{0}/v{1}'.format(
        app.config['API_PREFIX'],
        apiv1.VERSION
    )
)
