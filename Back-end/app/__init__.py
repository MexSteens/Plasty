from flask import Flask, jsonify, request
from app.config import Config
from flask_cors import CORS
from app.jwt import jwt
from app.database import db
from app.api import api
from webargs.flaskparser import parser, abort


# Initialize App
app = Flask(__name__, instance_relative_config=False)

# Load configurations from config.py
app.config.from_object(Config)

# Initialize JWT manager.
jwt.init_app(app)

# Initialize CORS extension
CORS(app)

# Initialize database connection.
db.init_app(app)

# Initialize API resources
api.init_app(app)


@app.route(Config.Api.path('test'))
def test():
    print(request.headers)
    return {'msg': 'ECHO TEST'}


# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)


@app.route('/', defaults={'path': '/'})
@app.route("/<path:path>")
def universal(path):
    response = jsonify(message=f"Endpoint '{path}' not found")
    response.status_code = 404

    return response
