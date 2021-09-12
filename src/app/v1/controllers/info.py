from ..models.device import Device as DeviceModel
from ..models.info import Info as InfoModel
from app import db
from datetime import datetime, timedelta
from sqlalchemy import desc

def create_info(info):
    device_id = info['device']
    gaz = info['gaz']
    speed = info['speed']
    water_lvl = info['water_lvl']
    water_temp = info['water_temp']
    water_press = info['water_press']
    oil_lvl = info['oil_lvl']
    oil_temp = info['oil_temp']
    oil_press = info['oil_press']
    #timestamp = info['timestamp']
    now = datetime.now()
    now1 = now + timedelta(hours=-1)

    device = DeviceModel.query.filter_by(UCID=device_id).first_or_404()
    info = InfoModel(gaz=gaz,speed=speed,water_lvl=water_lvl,water_temp=water_temp,water_press=water_press,oil_lvl=oil_lvl,oil_temp=oil_temp,oil_press=oil_press,timestamp=now1.strftime("%Y-%m-%dT%H:%M:%SZ"),device=device)
    db.session.add(info)
    db.session.commit() 
    return info


def get_info_device(device_id):
    device = DeviceModel.query.filter_by(UCID=device_id).first_or_404()
    info = InfoModel.query.filter_by(device=device).order_by(desc(InfoModel.timestamp)).first_or_404()
    return info

def get_all_info_device(device_id):
    device = DeviceModel.query.filter_by(UCID=device_id).first_or_404()
    info = InfoModel.query.filter_by(device=device).order_by(desc(InfoModel.timestamp)).all()
    return info