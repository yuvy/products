from db import db
from sqlalchemy import asc


class ProductsModel(db.Model):

    __tablename__ = 'prods'

    sno = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    brand = db.Column(db.String(1200))
    retailer = db.Column(db.String(1200))
    price = db.Column(db.Integer)
    instock = db.Column(db.String(500))

    def __init__(self, _id, name, brand, retailer, price, in_stock):
        """Initialize parameters"""
        self.id = _id
        self.name = name
        self.brand = brand
        self.retailer = retailer
        self.price = price
        self.inStock = in_stock

    def json(self):
        """JSON Representation"""
        d = {
            'id': str(self.id),
            'name': self.name or None,
            'brand': self.brand or None,
            'retailer': self.retailer or None,
            'price': float(self.price) if self.price else None,
            'in_stock': False if self.instock.lower() in ['n', 'no'] else True
        }

        return d


    @classmethod
    def find_product_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_cheapest_products(cls, n):
        return cls.query.filter(cls.price > 0).filter(cls.price != 'null').order_by(asc(cls.price)).limit(n).all()
