from app.api import MultiResource, SingleResource
from app.database.model import Company, Product
from webargs import fields, validate
from app.jwt import admin_required

args = {
    "name": fields.String(validate=validate.Length(min=1, max=128))
}


class CompaniesResource(MultiResource):
    parameters = args
    model = Company

    @admin_required()
    def post(self):
        return super().post()


class CompanyResource(SingleResource):
    parameters = args
    model = Company
    children = {
        'products': {
            'columns': Product.columns(),
            'read': model.read_products
        }
    }

    @admin_required()
    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)

    @admin_required()
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
