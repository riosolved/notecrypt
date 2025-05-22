import os
from flask import Flask
from flask_cors import CORS
import routes
import utilities

utilities.session.initialize(os.environ.get('SESSION_SECRET_KEY'))

utilities.database.initialize({
    "user": os.environ.get('PERSISTENCE_USER'),
    "password": os.environ.get('PERSISTENCE_PASSWORD'),
    "host": os.environ.get('PERSISTENCE_HOST'),
    "port": os.environ.get('PERSISTENCE_PORT'),
    "database": os.environ.get('PERSISTENCE_DATABASE')
})

application = Flask(__name__)

origins = [
    "https://client.localhost"
]

if os.environ.get('ENVIRONMENT') == 'local':
    origins.append("http://127.0.0.1")

CORS(
    application,
    origins=origins
)

application.register_blueprint(routes.api, url_prefix="/api")

application.run(host="0.0.0.0", port=5000, debug=True)
