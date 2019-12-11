"""
app.py

File with Flask EndPoints Defined

Python Version: 3.7
"""

from flask import Flask, jsonify
from flask_restful import Api, Resource

from db import db
from data_models import ProductsModel

PORT = 5001

app = Flask('products')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

db.init_app(app)

class GetProds(Resource):
    """
    Endpoint for products
    """
    @classmethod
    def get(cls, prod_id):
        prod = ProductsModel.find_product_by_id(prod_id)
        if not prod:
            return {'message': 'No Products found for: {}'.format(prod_id)}, 404
        return prod.json(), 200


class GetCheapProds(Resource):
    """
    Endpoint for cheapest products
    """
    @classmethod
    def get(cls, n):
        cheapest = ProductsModel.get_cheapest_products(n)
        if not cheapest:
            return {'message': 'None Found !!!'}, 404

        r = {'cheapest': [x.json() for x in cheapest]}

        return r, 200


class Home(Resource):
    @classmethod
    def get(cls):
        return jsonify({'msg': "Products RESTApi"})


# add endpoints
api.add_resource(GetProds, '/prod/<int:prod_id>')
api.add_resource(GetCheapProds, '/cheapest/<int:n>')
api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
