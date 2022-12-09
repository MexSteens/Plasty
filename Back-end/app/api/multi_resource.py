from flask import jsonify, abort, request, Response
from flask_restful import Resource
from app.config import Config
from sqlalchemy import exc
from webargs.flaskparser import parser
from webargs import fields, validate
from sqlalchemy_tables_extended import Export, Odata

class MultiResource(Resource):
    parameters = None
    model = None
    # limit = Config.Api.max_limit
    limit = 100
    excluded_columns = []
    children = {}
    get_show_children = False
    use_odata = True
    __odata = {
        "$skip": fields.Integer(validate=validate.Range(min=0), attribute="skip"),
        "$top": fields.Integer(validate=validate.Range(min=1, max=limit), attribute="top", missing=limit),
        "$filter": fields.DelimitedList(fields.String(), delimiter=' or ', attribute="filter"),
        "$select": fields.DelimitedList(fields.String(), delimiter=',', attribute="select"),
        "$orderby": fields.DelimitedList(fields.String(), delimiter=',', attribute="orderby"),
        "$count": fields.Boolean(attribute="count")
    }

    def generate_json(self, resource, show_children=True, columns=None):
        if columns is None:
            columns = self.model.columns(excluded=self.excluded_columns)
        else:
            columns = columns

        if show_children:
            json = []
            for item in resource:
                item_json = Export.json(item, columns=columns)
                for key, value in self.children.items():
                    if not callable(value):
                        item_json[key] = Export.json(value.get('read')(resource), columns=value.get('columns'))
                    else:
                        item_json[key] = value(item)

                json.append(item_json)
        else:
            json = Export.json(resource, columns=columns)

        return json

    def parameter_arguments(self):
        return parser.parse(self.parameters, request, location='json')

    def query_arguments(self):
        return parser.parse(self.__odata, request, location='query')

    def get(self):
        # Fetch data from database and return jsonify map.
        if self.use_odata:
            odata = Odata(self.model, self.model.query)
            args = self.query_arguments()

            if 'select' in args:
                odata.select(*[arg.strip() for arg in args.get('select')])

            if 'filter' in args:
                odata.filter(*args.get('filter'))

            if 'orderby' in args:
                odata.orderby(*args.get('orderby'))

            if 'skip' in args:
                odata.skip(args.get('skip'))

            if 'top' in args:
                odata.top(args.get('top'))

            if args.get('count'):
                return odata.count()

            return jsonify(self.generate_json(odata.query.all(), show_children=self.get_show_children, columns=args.get('select')))
        else:
            return jsonify(self.generate_json(self.model.read(), show_children=self.get_show_children))

    def post(self):
        # Parse arguments
        args = self.parameter_arguments()
        head_args = args.copy()

        for child in self.children:
            del head_args[child]

        # Construct the BO object.
        resource = self.model(**head_args)

        try:
            # Create object inside database.
            resource.create()

            for child, function in self.children.items():
                function.get('create')(resource, args.get(child))

            # Init json response/
            response = jsonify(self.generate_json(resource, show_children=False))
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.status_code = 201

            return response
        except exc.IntegrityError:
            # Return http status code 409 if database error happened.
            abort(409)
