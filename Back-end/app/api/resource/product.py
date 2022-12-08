from app.api import MultiResource, SingleResource
from app.database.model import Product, Complaint
from webargs import fields, validate
from app.jwt import admin_required

args = {
    "company_id": fields.Integer(),
    "name": fields.String(validate=validate.Length(min=1, max=128)),
    "barcode": fields.String(validate=validate.Length(min=1, max=32))
}


class ProductsResource(MultiResource):
    parameters = args
    model = Product
    get_show_children = True
    children = {
        "total_complaints": model.total_complaints
    }

    @admin_required()
    def post(self):
        return super().post()


class ProductResource(SingleResource):
    parameters = args
    model = Product
    children = {
        "complaints": {
            "columns": Complaint.columns(),
            "read": model.read_complaints
        },
        "total_complaints": model.total_complaints
    }

    @admin_required()
    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)

    @admin_required()
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)


class ProductBarcodeResource(ProductResource):
    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
