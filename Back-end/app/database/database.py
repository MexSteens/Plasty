from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Used for converting SQLAlchemy decimal object to a float.
# If a value from the record is null it will result into an error when converted to float using float()
# This method will return None if the record value is null otherwise it will convert the decimal to float.
def convert_float_safe(variable):
    output = None
    try:
        output = float(variable)
    except TypeError:
        output = None
    finally:
        return output
