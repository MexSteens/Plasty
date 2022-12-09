import configini
import os
import sqlalchemy.dialects.mysql

configini.read('config.ini')



class Config:
    """Set Flask configuration vars from .env file."""

    # Flask Config
    SECRET_KEY = configini.String('flask', 'secret_key', default=os.urandom(32))
    FLASK_APP = configini.String('flask', 'app', default='app')
    FLASK_ENV = configini.String('flask', 'env')
    FLASK_DEBUG = True
    MAX_CONTENT_LENGTH = configini.Integer('flask', 'max_content_length', default=16) * 1024 * 1024
    JWT_SECRET_KEY = configini.String('flask', 'secret_key', default=os.urandom(16))
    PROPAGATE_EXCEPTIONS = True

    class Api:
        _path = configini.String('api', 'path', default='api')
        delete_message = "Resource {} has been deleted."
        max_limit = configini.String('api', 'max_limit', default=500)

        @classmethod
        def path(cls, name):
            return f"/{cls._path}/{name}"

    class Database:
        dialect = configini.String('database', 'dialect', default='mysql')
        driver = configini.String('database', 'driver')
        username = configini.String('database', 'username')
        password = configini.String('database', 'password')
        hostname = configini.String('database', 'hostname', default='localhost')
        port = configini.String('database', 'port', default='3306')
        database = configini.String('database', 'database')

    class Plasty:
        off_api_url = configini.String('plasty', 'off_api_url')

    # Database Config
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{username}:{password}@{hostname}:{port}/{database}'.format(
        # dialect=Database.dialect,
        # driver=Database.driver,
        username=Database.username,
        password=Database.password,
        hostname=Database.hostname,
        port=Database.port,
        database=Database.database
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
