from flask import Blueprint

bp = Blueprint(
    "base",
    __name__,
    template_folder="templates",
    static_url_path="/base",
    static_folder="static",
)
