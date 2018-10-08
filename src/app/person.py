import os
import re
import uuid

from utils.settings import UPLOAD_DIRS
from flask import Blueprint, render_template, request, redirect
from src.model.person import Person


person_blueprint = Blueprint("person", __name__)


@person_blueprint.route("/rarity/")
def rarity():
    return render_template("person/rarity.html")


@person_blueprint.route("/person_detail/")
def person_detail():
    rarity = request.args.get("rarity")
    person = Person.objects.filter(rarity=rarity)
    return render_template("person/person_detail.html", person=person)


@person_blueprint.route("/add_person/", methods=["get", "post"])
def add_person():
    if request.method == "GET":
        return render_template("person/add_person.html")
    name = request.form.get("name")
    rarity = request.form.get("rarity").upper()
    skill_photo = request.files.get("skill_photo")
    skill = []
    if skill_photo:
        if not re.match(r'^image/.*$', skill_photo.mimetype):
            return "请上传正确的图片"
        photo_name = uuid.uuid1().hex + "." + skill_photo.filename.split(".")[-1]
        skill_url = os.path.join(UPLOAD_DIRS, photo_name)
        skill_photo.save(skill_url.replace("\\", "/"))
        skill_photo_url = os.path.join("/static/upload", photo_name).replace("\\", "/")
        skill.append(skill_photo_url)
    Person(name=name, rarity=rarity, skill=skill).save()
    return redirect("/person/rarity/")


@person_blueprint.route("/show_skill_photo/")
def show_skill_photo():
    id = request.args.get("id")
    person = Person.objects.filter(id=id).first()
    skill_urls = person.skill
    return render_template("person/skill_photo.html", skill_urls=skill_urls, person=person)


@person_blueprint.route("/add_skill_photo/", methods=["post"])
def add_skill_photo():
    id = request.form.get("id")
    skill_photo = request.files.get("skill_photo")
    if skill_photo:
        if not re.match(r'^image/.*$', skill_photo.mimetype):
            return "请上传正确的图片"
        photo_name = uuid.uuid1().hex + "." + skill_photo.filename.split(".")[-1]
        skill_url = os.path.join(UPLOAD_DIRS, photo_name)
        skill_photo.save(skill_url.replace("\\", "/"))
        skill_photo_url = os.path.join("/static/upload", photo_name).replace("\\", "/")
        person = Person.objects.filter(id=id).first()
        skill = person.skill
        skill.append(skill_photo_url)
        person.update(skill=skill)

    return redirect("/person/show_skill_photo/?id={}".format(id))



