from functools import wraps
from flask import g, flash, redirect, url_for, request

from app.users import constraints

def requires_admin(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user.role is not constraints.ADMIN:
			flash('You do not have the appropriate permissions to view this pagea'
			, 'alert-warning')
			return redirect(url_for('users.swampNuts'))
		return f(*args, **kwargs)
		return decorated_function
