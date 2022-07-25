from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(config.Config)
app.app_context().push()
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

from . import routes, models


