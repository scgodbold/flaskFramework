from flask import render_template, flash, redirect, request, g, session, Blueprint, url_for
from flask.ext.login import login_required, login_user, logout_user, current_user
from werkzeug import check_password_hash, generate_password_hash

# from app import db, lm
from app import lm
from app.users.models import User

users = Blueprint('users',__name__, url_prefix='/users')

@lm.user_loader
def loadUser(user):
	return User(uid=user)

@users.before_request
def before_request():
	g.user = current_user

@users.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		user = User(name=request.form['username'], passwd = request.form['passwd'])
		if user.is_active():
			login_user(user)
			redirect(url_for('frontend.home'))
	redirect(url_for('frontend.login'))
	

@users.route('/logout',methods=['GET','POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('frontend.index'))
