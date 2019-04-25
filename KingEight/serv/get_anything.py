from flask import Blueprint, request, jsonify, send_file
from settings import IMAGE_PATH, MUSIC_PATH
import os

get_any = Blueprint("get_any", __name__)


@get_any.route("/get_music/<filename>")
def get_music(filename):
    filename = os.path.join(MUSIC_PATH, filename)
    return send_file(filename)


@get_any.route("/get_image/<filename>")
def get_image(filename):
    filename = os.path.join(IMAGE_PATH, filename)
    return send_file(filename)
