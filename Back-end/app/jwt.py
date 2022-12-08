from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from flask import abort
from functools import wraps

jwt = JWTManager()


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            identity = get_jwt_identity()

            if not identity["admin"]:
                abort(403, description="Only Admins can perform this action.")

            return fn(*args, **kwargs)

        return decorator

    return wrapper


# def protected_user_required():
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args, **kwargs):
#             identity = get_jwt_identity()
#
#             if identity.get('id') != id and not identity.get('admin'):
#                 abort(403)
#
#             return fn(*args, **kwargs)
#
#         return decorator
#
#     return wrapper
