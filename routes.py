from flask import render_template, redirect, url_for, flash,request,current_app,Flask
from flask_login import login_user, logout_user, login_required, current_user,LoginManager,UserMixin


from __init__ import  app




#home
@app.route('/')
def home():    
    return render_template('index.html')

#adminlogin
@app.route('/adminlogin')
def admin_login():
    return render_template('admin_login.html')

@app.route('/check_admin',methods=['GET','POST'])
def check_admin():
	if request.method=='GET':
		return "Please go back to the admin login page and fill the credentials"
	else:
		uname = request.form['uname']
		password = request.form['pass']
		if uname == 'rojee' and password=='123':
			
			try :
				uid = int(password)
				# login_user(uid)
				return"success login"
			except Exception as e:
				print (e)

	return 'hi'

#admin query

@app.route('/adminquery')
def admin_query():
	# admin = redirect(url_for(check_admin))
	if admin=="success login":
		return "Welcome onboard"
	else :
		check_admin()
	return check_admin()

#customer
@app.route('/customerlogin')
def customer_login():
    return render_template('customer_login.html')




