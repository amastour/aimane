from flask_restx import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
from app.v1 import auth_api


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    gaz = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    water_lvl = db.Column(db.Integer, nullable=False)
    water_temp = db.Column(db.Integer, nullable=False)
    water_press = db.Column(db.Integer, nullable=False)
    oil_lvl = db.Column(db.Integer, nullable=False)
    oil_temp = db.Column(db.Integer, nullable=False)
    oil_press = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable = False)

    device_id = db.Column(db.Integer, ForeignKey('device.UCID'))
    device = relationship("Device", back_populates="datas")

    data_resource_model = auth_api.model('Data', {
        'gaz': fields.Integer(required=True),
        'speed': fields.Integer(required=True),
        'water_lvl': fields.Integer(required=True),
        'water_temp': fields.Integer(required=True),
        'water_press': fields.Integer(required=True),
        'oil_lvl': fields.Integer(required=True),
        'oil_temp': fields.Integer(required=True),
        'oil_press': fields.Integer(required=True),
        'timestamp': fields.DateTime(),
        'device': fields.String(attribute='device.UCID'),
    })

