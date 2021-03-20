import sqlite3


from flask_login import UserMixin
from __init__ import app,db
from flask_login import LoginManager

def createtable():
	conn = sqlite3.connect('Admin.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE user(id INTEGER PRIMARY KEY,uname TEXT NOT NULL,password UNIQUE NOT NULL )")
	conn.commit()
	conn.close()
	return "table created"

def insert():
	conn = sqlite3.connect("Admin.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO user VALUES(11,'rojee2','password2')")
	conn.commit()
	conn.close()
	return "success"

def fetch():
	conn = sqlite3.connect("Admin.db")
	cur = conn.cursor()
	cur.execute("SELECT password FROM user WHERE uname='rojee4'")
	data = cur.fetchall()
	conn.commit()
	conn.close()
	if len(data)==0:
		print ("data list is empty")
	else:
		print("Printing the required data...")
	return data

def iduser():
	conn = sqlite3.connect("Admin.db")
	cur = conn.cursor()
	cur.execute("SELECT id FROM user WHERE uname='rojee'")
	data = cur.fetchall()
	conn.commit()
	conn.close()
	if len(data)==0:
		print ("data list is empty")
	else:
		print("Printing the required data...")
	print(type(data[0]))
	return data

log_man = LoginManager(app)
log_man.init_app(app)


@log_man.user_loader
def load_Admin(user_id):
    return Admin.query.get(user_id)




class Admin(db.Model,UserMixin):
	"""docstring for ClassName"""
	__tablename__ = 'Admin'

	id = db.Column(db.Integer,primary_key=True)
	uname = db.Column(db.String, nullable=False)
	password = db.Column(db.String,  nullable=False)

class Customer(db.Model,UserMixin):
	"""docstring for ClassName"""
	__tablename__ = 'Customer'

	id = db.Column(db.Integer,primary_key=True)
	uname = db.Column(db.String, nullable=False)
	camper_order = db.Column(db.Integer,nullable=False)
	time_diliv = db.Column(db.String,nullable=False)
	


if __name__ == '__main__':
	print(iduser())


	  