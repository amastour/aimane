from flask import request
from flask_restx import Resource, Namespace
from ..models.info import Info as InfoModel
from ..controllers.info import  create_info, get_info_device, get_all_info_device
from app.v1 import auth_api
from datetime import datetime

import logging
log = logging.getLogger(__name__)


info_ns = Namespace("info", "info operations")

@info_ns.route('/')
class InfoList(Resource):

    @info_ns.expect(InfoModel.info_resource_model, validate=True)
    @info_ns.marshal_with(InfoModel.info_resource_model)
    def post(self):
        """Create a new device"""
        dev = create_info(auth_api.payload)
        return dev, 200


@info_ns.route('/<string:id>')
class Device(Resource):
    @info_ns.response(404, 'Device not found or you don\'t have permission to view it')
    @info_ns.marshal_with(InfoModel.info_resource_model)
    def get(self, id):
        """Get one task"""
        dev = get_info_device(id)
        return dev

@info_ns.route('/all/<string:id>')
class DeviceAll(Resource):
    @info_ns.response(404, 'Device not found or you don\'t have permission to view it')
    @info_ns.marshal_with(InfoModel.info_resource_model)
    def get(self, id):
        """Get one task"""
        dev = get_all_info_device(id)
        return dev