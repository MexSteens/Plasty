from flask import jsonify, abort, request
from flask_restful import Resource
from app.config import Config
from sqlalchemy import exc, inspection
from webargs.flaskparser import parser
from webargs import fields, validate
from sqlalchemy_tables_extended import Export, Odata


class SingleResource(Resource):
    parameters = None
    model = None
    children = {}
    excluded_columns = []
    schema = None
    use_odata = True
    __odata = {
        "$select": fields.DelimitedList(fields.String(), delimiter=',', attribute="select")
    }

    def generate_json(self, resource, show_children=True, columns=None):
        if columns is None:
            columns = self.model.columns(excluded=self.excluded_columns)
        else:
            columns = columns

        json = Export.json(resource, columns=columns)

        if show_children:
            for key, value in self.children.items():
                if not callable(value):
                    json[key] = Export.json(value.get('read')(resource), columns=value.get('columns'))
                else:
                    json[key] = value(resource)

        return json

    def parameter_arguments(self):
        return parser.parse(self.parameters, request, location='json')

    def query_arguments(self):
        return parser.parse(self.__odata, request, location='query')

    def get(self, *args, **kwargs):
        resource = self.model.get(*args, **kwargs)

        if resource:
            if self.use_odata:
                odata = Odata(self.model, self.model.query)
                odata_args = self.query_arguments()

                if 'select' in odata_args:
                    odata.select(*[arg.strip() for arg in odata_args.get('select')])

                    return jsonify(self.generate_json(resource, columns=odata_args.get('select')))

            return jsonify(self.generate_json(resource))
        else:
            abort(404)

    def put(self, *args, **kwargs):
        resource = self.model.get(*args, **kwargs)

        if resource:
            args = self.parameter_arguments()
            head_args = args.copy()

            for child, function in self.children.items():
                if 'update' in function:
                    del head_args[child]

            try:
                resource.update(**head_args)

                for child, function in self.children.items():
                    if 'update' in function:
                        function.get('update')(resource, args.get(child))

                response = jsonify(self.generate_json(resource))
                response.headers.add('Access-Control-Allow-Origin', '*')
                response.status_code = 201

                return response
            except exc.IntegrityError:
                abort(409)
        else:
            abort(404)

    def delete(self, *args, **kwargs):
        resource = self.model.get(*args, **kwargs)

        if resource:
            try:
                resource.delete()

                response = jsonify(message=Config.Api.delete_message.format(resource))
                response.headers.add('Access-Control-Allow-Origin', '*')
                response.status_code = 201

                return response
            except exc.IntegrityError:
                abort(409)
        else:
            abort(404)
