from .base_mongo import db


class Person(db.Document):

    meta = {"collection": "person"}
    name = db.StringField(required=True, verbose_name="名称")
    rarity = db.StringField(required=True, verbose_name="稀有度")
    skill = db.ListField(db.StringField(), required=True, verbose_name="技能")
