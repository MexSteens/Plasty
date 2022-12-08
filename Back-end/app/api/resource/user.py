from flask import jsonify, abort
from app.api import MultiResource, SingleResource
from app.database.model import User, Product
from webargs import fields, validate
from flask_jwt_extended import jwt_required
from sqlalchemy import exc
from app.jwt import admin_required
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

post_args = {
    "name": fields.String(validate=validate.Length(min=1, max=128), required=True),
    "email": fields.Email(required=True),
    "password": fields.String(validate=validate.Length(min=1, max=512), required=True),
    "admin": fields.Boolean(default=False, missing=False)
}

put_args = {
    "name": fields.String(validate=validate.Length(min=1, max=128), required=True),
    "email": fields.Email(required=True),
    "admin": fields.Boolean(default=False, missing=False)
}

password_args = {
    "password": fields.String(validate=validate.Length(min=1, max=512), required=True)
}


class UsersResource(MultiResource):
    parameters = post_args
    model = User
    excluded_columns = ['password']

    @admin_required()
    def get(self):
        return super().get()

    def post(self):
        # Parse arguments
        args = self.parameter_arguments()

        # Construct the BO object.
        resource = self.model(**args)
        resource.set_password(args.get('password'))

        verify_jwt_in_request(optional=True)
        identity = get_jwt_identity()

        # If user is not logged in or is not an admin then set admin to False.
        if not identity or not identity.get('admin'):
            resource.admin = False

        # If user does not exist create a new one.
        if not User.get(email=args.get('email')):
            try:
                # Create object inside database.
                resource.create()

                # Init json response
                response = jsonify(self.generate_json(resource, show_children=False))
                response.status_code = 201

                return response
            except exc.IntegrityError:
                # Return http status code 409 if database error happened.
                abort(409)
        else:
            abort(409, description="User already exists.")


class UserResource(SingleResource):
    parameters = put_args
    model = User
    children = {
        'scanned_products': {
            'columns': Product.columns(),
            'read': model.scanned_products
        },
        'achievements': model.get_achievements
    }
    excluded_columns = ['password']

    @jwt_required()
    def get(self, id):
        identity = get_jwt_identity()

        if identity.get('id') != id and not identity.get('admin'):
            abort(403)

        return super().get(id=id)

    @jwt_required()
    def put(self, id):
        identity = get_jwt_identity()

        if identity.get('id') != id and not identity.get('admin'):
            abort(403)

        return super().put(id=id)

    @jwt_required(fresh=True)
    def delete(self, id):
        identity = get_jwt_identity()

        if identity.get('id') != id and not identity.get('admin'):
            abort(403)

        return super().delete(id=id)


class PasswordResetResource(SingleResource):
    parameters = password_args
    model = User

    def get(self):
        pass

    @jwt_required(fresh=True)
    def put(self, id):
        resource = self.model.get(id=id)

        identity = get_jwt_identity()
        if identity.get('id') != id and not identity.get('admin'):
            abort(403)

        if resource:
            args = self.parameter_arguments()

            try:
                resource.set_password(args.get('password'))
                resource.update()

                response = jsonify(message="Password has been changed.")
                response.status_code = 201

                return response
            except exc.IntegrityError:
                abort(409)
        else:
            abort(404)

    def delete(self):
        pass
