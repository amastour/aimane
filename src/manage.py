import os

from flask_script import Manager
from flask import jsonify

from app import create_app, db

env = os.getenv("CONFIG_TYPE") or "dev"
app = create_app(env)
manager = Manager(app)

@app.route("/ping")
def ping():
    return jsonify("pong")

@manager.command
def db_init():
    db.create_all()


@manager.command
def run():
    """Like a 'runserver' command but shorter, lol."""
    app.run(host="0.0.0.0")


if __name__ == '__main__':
    manager.run()
