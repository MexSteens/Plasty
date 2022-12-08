import logging
from flask import abort, jsonify, request
from sqlalchemy_tables_extended import Export
from flask_restful import Resource
from app.database.model import User, Company, Product, Complaint
from webargs import fields, validate
from webargs.flaskparser import parser
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.config import Config
import requests
from app.rewards import AchievementChecker, LevelChecker, StreakChecker

product_args = {
    "company_name": fields.String(validate=validate.Length(min=1, max=128)),
    "product_name": fields.String(validate=validate.Length(min=1, max=128))
}


class ScanResource(Resource):
    @jwt_required()
    def post(self, barcode):
        # Fetch user data.
        identity = get_jwt_identity()

        user = User.get(id=identity.get('id'))

        product = Product.get(barcode=barcode)

        rewards = {
            'experience_gained': []
        }

        if not product:
            try:
                off_product = requests.get(Config.Plasty.off_api_url.format(barcode=barcode), timeout=5)
            except requests.exceptions.Timeout:
                logging.error("Connection timed out to the Open Food Facts API.")
                abort(500, description="Connection timed out to the Open Food Facts API. Try again later.")

            off_product_json = off_product.json()

            # Check if a valid product has been found.
            if off_product_json.get('status') == 0:
                abort(400,
                      description="Product not found inside Open Food Facts Database, please specify more information.")

            # Fetch product name & brand.
            off_product_brand = off_product_json.get('product').get('brands')
            off_product_name = off_product_json.get('product').get('product_name')

            # Check if company exists.
            if off_product_brand:
                company = Company.get(name=off_product_brand)

                # Create a new company if it does not exist.
                if not company:
                    company = Company(name=off_product_brand)
                    company.create()
            else:
                # The OFF_product has no brand then assign it to unknown brand.
                company = Company(id=0)

            # Create new product.
            product = Product(company_id=company.id, name=off_product_name, barcode=barcode)
            product.create()

            # 5 xp bonus for scanning a new product.
            user.exp_gain(5)
            rewards['experience_gained'].append(['New product bonus', 5])

        # Create new complaint
        complaint = product.new_complaint(user_id=identity.get('id'))

        # 10 xp bonus for scanning a product.
        user.exp_gain(10)
        rewards['experience_gained'].append(['Scan bonus', 10])

        # Check for rewards.
        if streaks_gained := StreakChecker(user):
            rewards['streaks_gained'] = streaks_gained
            user.exp_gain(5)
            rewards['experience_gained'].append(['Streak bonus', 5])

        if achievements_gained := AchievementChecker(user):
            rewards['achievements_gained'] = []
            for achievements in achievements_gained:
                rewards['achievements_gained'].append(achievements[0])
                rewards['experience_gained'].append(['Achievement bonus', achievements[1]])

        if levels_gained := LevelChecker(user):
            rewards['levels_gained'] = levels_gained

        user.update()

        export = Export.json(complaint, columns=Complaint.columns())
        export['rewards'] = rewards

        response = jsonify(export)
        response.status_code = 201

        return response


class NewScanResource(Resource):
    @jwt_required()
    def post(self, barcode):
        # Fetch user data.
        identity = get_jwt_identity()

        args = parser.parse(product_args, request, location='json')

        company = Company.get(name=args.get('company_name'))

        if not company:
            company = Company(name=args.get('company_name'))
            company.create()

        product = Product(company_id=company.id, name=args.get('product_name'), barcode=barcode)
        product.create()

        # Create new complaint and return it.
        response = jsonify(Export.json(product.new_complaint(user_id=identity.get('id')), columns=Complaint.columns()))

        response.status_code = 201

        return response
