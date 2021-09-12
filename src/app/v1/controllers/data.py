from ..models.device import Device as DeviceModel
from ..models.data import Data as DataModel
from app import db
from datetime import datetime, timezone
from sqlalchemy import desc

def create_data(data):
    device_id = data['device']
    gaz = data['gaz']
    speed = data['speed']
    water_lvl = data['water_lvl']
    water_temp = data['water_temp']
    water_press = data['water_press']
    oil_lvl = data['oil_lvl']
    oil_temp = data['oil_temp']
    oil_press = data['oil_press']
    #timestamp = data['timestamp']

    device = DeviceModel.query.filter_by(UCID=device_id).first_or_404()
    data = DataModel(gaz=gaz,speed=speed,water_lvl=water_lvl,water_temp=water_temp,water_press=water_press,oil_lvl=oil_lvl,oil_temp=oil_temp,oil_press=oil_press,timestamp=datetime.now(),device=device)
    db.session.add(data)
    db.session.commit() 
    return data


def get_data_device(device_id):
    device = DeviceModel.query.filter_by(UCID=device_id).first_or_404()
    data = DataModel.query.filter_by(device=device).order_by(desc(DataModel.timestamp)).first_or_404()
    return data

def get_all_data_device(device_id):
    device = DeviceModel.query.filter_by(UCID=device_id).first_or_404()
    data = DataModel.query.filter_by(device=device).order_by(desc(DataModel.timestamp)).all()
    return data