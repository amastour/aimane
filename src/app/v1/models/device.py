from enum import unique
from flask_restx import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
from app.v1 import auth_api
#from ..models.product import Product

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    UCID = db.Column(db.String(5), nullable=False, unique=True)
    status = db.Column(db.Boolean(), default=True)
    activation = db.Column(db.Boolean(), default=True)
    creation_date = db.Column(db.DateTime, nullable = False)

    datas = relationship("Data", back_populates="device")


    device_resource_model= auth_api.model('device', {
        'UCID': fields.String(required=True, description='The Device unique identifier. ReadOnly.'),
        'activation': fields.Boolean( description='Status of collect for device'),
        'creation_date': fields.DateTime( description='Creation date of  device'),
    })
    

    device_create_resource_model= auth_api.model('device_create', {
        'UCID': fields.String(required=True, description='The Universal Cars Identifier'),
    })
    
    # products_resource_model = v1_api.inherit('products resource model', device_resource_model, {
    #     'products' :  fields.List(fields.Nested(Product.product_resource_model))
    # })
