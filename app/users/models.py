from flask_login import UserMixin

# from app import db

# class User(db.Model, UserMixin):
class User(UserMixin):
	def __init__(self, uid=None, name=None, passwd=None):
		self.active = False
		self.uid = 0
		self.uid = uid
		self.name = name
		self.passwd = passwd
		if passwd == 'swordfish' pr self.uid == 1:
			# Change this to mirror appropriate login stuff
			self.uid = 1
			self.active = True
	
	def is_active(self):
		return self.active

	def get_name(self):
		return self.name

	def get_admin(self):
		# Obviously this is bad
		return True
