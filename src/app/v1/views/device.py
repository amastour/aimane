from flask import request
from flask_restx import Resource, Namespace
from ..models.device import Device as DeviceModel
from ..controllers.device import  get_device, create_device,update_device,delete_device
from app.v1 import auth_api
from datetime import datetime

import logging
log = logging.getLogger(__name__)


device_ns = Namespace("device", "device operations")

@device_ns.route('/')
class DeviceList(Resource):
    @device_ns.marshal_with(DeviceModel.device_resource_model)
    def get(self):
        """Get Devices list"""
        devs = get_device()
        return devs

    @device_ns.expect(DeviceModel.device_create_resource_model, validate=True)
    @device_ns.marshal_with(DeviceModel.device_create_resource_model)
    def post(self):
        """Create a new device"""
        dev = create_device(auth_api.payload)
        return dev, 200


@device_ns.route('/<string:id>')
class Device(Resource):
    @device_ns.response(404, 'Device not found or you don\'t have permission to view it')
    @device_ns.marshal_with(DeviceModel.device_resource_model)
    def get(self, id):
        """Get one task"""
        dev = get_device(id)
        return dev

    @device_ns.response(404, 'Device not found or you don\'t have permission to edit it')
    @device_ns.response(201, 'Device successfully updated.')
    @device_ns.expect(DeviceModel.device_resource_model, validate=True)
    @device_ns.marshal_with(DeviceModel.device_resource_model)
    def put(self, id):
        """Get one Device"""

        dev = update_device(id, auth_api.payload)
        return dev

    @device_ns.response(404, 'Device not found or you don\'t have permission to delete it')
    @device_ns.response(204, 'Device deleted')
    def delete(self, id):
        """Delete one Device"""
        delete_device(id)

        return '', 204
