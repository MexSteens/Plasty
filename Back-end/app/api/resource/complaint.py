from app.api import MultiResource, SingleResource
from app.database.model import Complaint
from webargs import fields
from app.jwt import admin_required

args = {
    "product_id": fields.Integer()
}


class ComplaintsResource(MultiResource):
    parameters = args
    model = Complaint

    @admin_required()
    def post(self):
        return super().post()


class ComplaintResource(SingleResource):
    parameters = args
    model = Complaint

    @admin_required()
    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)

    @admin_required()
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
