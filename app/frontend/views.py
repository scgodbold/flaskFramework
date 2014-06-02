from flask import render_template, flash, redirect, \
		request, g, session, Blueprint, url_for

# Uncomment for user auth
# from flask.ext.login import current_user

# Uncomment for database support
# from app import db

frontend = Blueprint('frontend', __name__)

"""
Used for user auth uncomment for user auth
@frontend.before_request
def before_request():
	g.user = current_user
"""

@frontend.route('/')
def index():
	return render_template('frontend/index.html')

@frontend.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html')
