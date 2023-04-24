from flask import Flask
from .config import Config
from .models import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    migrate = Migrate(app, db)
    db.init_app(app)

    from .base import bp as base_bp

    app.register_blueprint(base_bp, url_prefix="/base")

    from .main import bp as main_bp

    app.register_blueprint(main_bp, url_prefix="/")

    from .auth import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    from .editor import bp as editor_bp

    app.register_blueprint(editor_bp, url_prefix="/editor")

    return app
