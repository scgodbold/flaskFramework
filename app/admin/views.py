from flask import render_template, flash, redirect, \
		request, g, session, Blueprint, url_for

# Uncomment for user auth
# from flask.ext.login import current_user

# Uncomment for database support
# from app import db

admin = Blueprint('admin', __name__, url_prefix='/admin')

"""
Used for user auth uncomment for user auth
@admin.before_request
def before_request():
	g.user = current_user
"""

@admin.route('/')
def index():
	return render_template('admin/adminbase.html')
