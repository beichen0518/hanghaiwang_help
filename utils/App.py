from flask import Flask

from utils.settings import templates_dir, static_dir
from utils.functions import init_ext
from src.app.person import person_blueprint
from mongoengine import connect


def create_app(config):

    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    app.register_blueprint(blueprint=person_blueprint, url_prefix='/person')
    connect("hanghaiwang", host="47.98.172.171", port=27017)
    app.config.from_object(config)
    init_ext(app)

    return app