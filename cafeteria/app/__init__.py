import logging

from flask import Flask
from flask_appbuilder import AppBuilder
from flask_appbuilder.models.sqla.base import SQLA
from .security import CustomSecurityManager

# Logging configuration
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)

with app.app_context():
    from .index_view import MyIndexView
    appbuilder = AppBuilder(app, db.session, security_manager_class=CustomSecurityManager, indexview=MyIndexView)
    from . import views
