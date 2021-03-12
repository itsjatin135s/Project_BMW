import sqlite3

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

if __name__ == '__main__':
	print(fetch())


	  