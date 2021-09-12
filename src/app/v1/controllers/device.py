from ..models.device import Device as DeviceModel
from app import db
from datetime import datetime

def get_device(device_id=None):
    if device_id is None:
        device = DeviceModel.query.filter_by(status=True).all()
    else:
        device = DeviceModel.query.filter_by(UCID=device_id).first_or_404()
    return device

def create_device(data):
    UCID = data["UCID"]
    device= DeviceModel(UCID=UCID,creation_date= datetime.utcnow())
    db.session.add(device)
    db.session.commit()
    return device


def update_device(device_id,data):
    dev = DeviceModel.query.filter_by(UCID=device_id).first_or_404()

    if 'activation' in data:
        dev.activation= data['activation']

    db.session.add(dev)
    db.session.commit()

    return dev

def delete_device(device_id):
    dev = DeviceModel.query.filter_by(UCID=device_id).first_or_404()

    dev.status= False

    db.session.add(dev)
    db.session.commit()

    return dev