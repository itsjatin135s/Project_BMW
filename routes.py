from flask import render_template, redirect, url_for, flash,request,current_app,Flask,jsonify
from flask_login import login_user, logout_user, login_required, current_user,LoginManager,UserMixin 
from database_handler import iduser,log_man,Admin,Customer

from __init__ import  app,db

	
		


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
		user = Admin.query.filter_by(uname=uname).first()
		if user and user.password == password:
				login_user(user)
				return jsonify({'Login_Status':True,'Admin_Details':{'Username':user.uname,'Pass':user.password}})
		else:
			return "Invalid Credentials"	
	return password

#admin query
@app.route('/adminquery')
@login_required
def admin_query():
	return "succes"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

#add customer

@app.route('/add_customer',methods=['GET','POST'])
@login_required
def add_cust():
	if request.method=='POST':
		uname = request.form['uname']
		camp_odr = request.form['camp']
		tim_dliv = request.form['tim_dliv']
		user = Customer(uname=uname,
                    camper_order = camp_odr, time_diliv=tim_dliv)
		db.session.add(user)
		db.session.commit()
		return jsonify({'Login_Status':True,'Admin_Details':{'Username':user.uname,'Camper':user.camper_order}}
		)

	return render_template('add_cust.html')

#customer details
@app.route('/customer_details',methods=['GET','POST'])
@login_required
def cust_detail():
	if request.method=='POST':
		uname = request.form['uname']
		user = Customer.query.filter_by(uname=uname).all()
		users_dict = []
		print(user)

		for user1 in user:
			u1 = {'Login_Status':True,'Admin_Details':{'Username':user1.uname,'Camper':user1.camper_order}}
			print(u1)
		return "returned"

	return render_template('cust_detail.html')
		



