from app.api import MultiResource, SingleResource
from app.database.model import Achievement
from webargs import fields, validate
from app.jwt import admin_required

args = {
    "name": fields.String(validate=validate.Length(min=1, max=128)),
    "description": fields.String(),
    "experience_given": fields.Integer(validate=validate.Range(min=0))
}


class AchievementsResource(MultiResource):
    parameters = args
    model = Achievement

    @admin_required()
    def post(self):
        return super().post()


class AchievementResource(SingleResource):
    parameters = args
    model = Achievement

    @admin_required()
    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)

    @admin_required()
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
