from flask_restful import Api
from app.api.resource import *
from app.config import Config

# Initialize API resource with the CSRF exempt decorators
api = Api()

# Add all resource links
api.add_resource(CompaniesResource, Config.Api.path('company'))
api.add_resource(CompanyResource, Config.Api.path('company/<int:id>'))

api.add_resource(ProductsResource, Config.Api.path('product'))
api.add_resource(ProductResource, Config.Api.path('product/<int:id>'))

api.add_resource(ProductBarcodeResource, Config.Api.path('product_barcode/<string:barcode>'))

api.add_resource(AchievementsResource, Config.Api.path('achievement'))
api.add_resource(AchievementResource, Config.Api.path('achievement/<string:code>'))

api.add_resource(ComplaintsResource, Config.Api.path('complaint'))
api.add_resource(ComplaintResource, Config.Api.path('complaint/<int:id>'))

api.add_resource(UsersResource, Config.Api.path('user'))
api.add_resource(UserResource, Config.Api.path('user/<string:id>'))
api.add_resource(PasswordResetResource, Config.Api.path('user/password_reset/<string:id>'))

api.add_resource(AuthResource, Config.Api.path('auth'))
api.add_resource(RefreshResource, Config.Api.path('refresh'))

api.add_resource(ScanResource, Config.Api.path('scan/<string:barcode>'))
api.add_resource(NewScanResource, Config.Api.path('new_scan/<string:barcode>'))
