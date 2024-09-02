from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.config import config_options
from app.post import post_blueprint
def create_app (config_name="production"):
    app=Flask(__name__)
    current_config = config_options[config_name] 
    app.config.from_object(current_config)
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(post_blueprint)
    return app


