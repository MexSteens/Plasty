from flask import jsonify, abort, request
from app.database.model import User
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import parser
from datetime import timedelta
import logging
from flask_cors import cross_origin

auth_args = {
    "email": fields.Email(),
    "password": fields.String(validate=validate.Length(min=1, max=512))
}

class AuthResource(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()

        current_user = User.get(id=identity['id'])

        return jsonify(current_user.identity())

    def post(self):
        args = parser.parse(auth_args, request, location='json')

        try:
            with User.authenticate(args.get('email'), args.get('password')) as user:
                access_token = create_access_token(identity=user.identity(), fresh=True, expires_delta=timedelta(days=365))
                refresh_token = create_refresh_token(identity=user.identity())

                response = jsonify(access_token=access_token, refresh_token=refresh_token)
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response
        except LookupError:
            logging.warning(f"Attempted login on user: '{args.get('email')}' (User not found)")
            abort(401)
        except UserWarning:
            logging.warning(f"Attempted login on user: '{args.get('email')}' (Invalid password)")
            abort(401)


class RefreshResource(Resource):
    @jwt_required(refresh=True)
    @cross_origin()
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        return jsonify(access_token=access_token)
