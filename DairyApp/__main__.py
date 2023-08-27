""" Main file for Dairy App """

from flask import Flask
from DairyApp.api import api_v1

from DairyApp.libs.dblib.base import Base, engine

# Todo - read app configuration from config.py file
def configure_app(_flask_app):
    """Configure flask app configurations"""
    
    _flask_app.config["SWAGGER_UI_DOC_EXPANTION"] = "list"
    _flask_app.config["RESTX_VALIDATE"] = True
    _flask_app.config["RESTX_MASK_SWAGGER"] = False
    _flask_app.config["ERROR_404_HELP"] = False
    _flask_app.config["SWAGGER_UI_JSONEDITOR"] = False
    #_flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a@localhost/dairyappdb'


def make_app(config_name=None):  # config_name can be dev or production
    """Create app with flask"""
    # config = config_by_name[config_name]

    app = Flask("Dairy App")
    configure_app(app)

    # app.config.from_object(config)
    app.register_blueprint(api_v1)

    with app.app_context():
        app.extensions["Test instance"] = "Test instance value"

    # generate database schema
    Base.metadata.create_all(engine)

    return app


def main():
    """Run server"""

    app = make_app()
    host = "0.0.0.0"
    port = 8000
    app.run(host=host, port=port)


if __name__ == "main":
    main()
