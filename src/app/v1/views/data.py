from flask import request
from flask_restx import Resource, Namespace
from ..models.data import Data as DataModel
from ..controllers.data import  create_data, get_data_device, get_all_data_device
from app.v1 import auth_api
from datetime import datetime

import logging
log = logging.getLogger(__name__)


data_ns = Namespace("data", "data operations")

@data_ns.route('/')
class DataList(Resource):

    @data_ns.expect(DataModel.data_resource_model, validate=True)
    @data_ns.marshal_with(DataModel.data_resource_model)
    def post(self):
        """Create a new device"""
        dev = create_data(auth_api.payload)
        return dev, 200


@data_ns.route('/<string:id>')
class Device(Resource):
    @data_ns.response(404, 'Device not found or you don\'t have permission to view it')
    @data_ns.marshal_with(DataModel.data_resource_model)
    def get(self, id):
        """Get one task"""
        dev = get_data_device(id)
        return dev

@data_ns.route('/all/<string:id>')
class DeviceAll(Resource):
    @data_ns.response(404, 'Device not found or you don\'t have permission to view it')
    @data_ns.marshal_with(DataModel.data_resource_model)
    def get(self, id):
        """Get one task"""
        dev = get_all_data_device(id)
        return dev