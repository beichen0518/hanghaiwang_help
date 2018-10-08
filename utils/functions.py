from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def get_db_uri(DATABASE):

    user = DATABASE.get('USER')
    db = DATABASE.get('DB')
    port = DATABASE.get('PORT')
    host = DATABASE.get('HOST')
    password = DATABASE.get('PASSWORD')
    name = DATABASE.get('NAME')
    driver = DATABASE.get('DRIVER')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver, user, password, host, port, name)


def init_ext(app):

    db.init_app(app=app)


