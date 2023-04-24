from flask import Blueprint

bp = Blueprint("editor", __name__, template_folder="templates", static_folder="static")

from . import views
