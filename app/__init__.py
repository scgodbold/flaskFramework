from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

# Uncomment to enable a database that is configured in config.py
# db = SQLAlchemy(app)

# Uncomment to enable user authentication
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'users.login'
# from app.users.views import users
# app.register_blueprint(users)

# Uncomment to enable an admin panel and interface 
from app.admin.views import admin
app.register_blueprint(admin)

# Default frontend application what the user sees
from app.frontend.views import frontend
app.register_blueprint(frontend)

