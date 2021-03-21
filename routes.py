from flask import render_template, redirect, url_for, flash,request,current_app,Flask,jsonify
from flask_login import login_user, logout_user, login_required, current_user,LoginManager,UserMixin 
from database_handler import iduser,log_man,Admin,Customer

from __init__ import  app,db


#home
@app.route('/')
def home():    
    return render_template('index.html')



#adminlogin
@app.route('/adminlogin',methods=['GET','POST'])
def admin_login():
	if request.method=='POST':
		uname = request.form['uname']
		password = request.form['pass']
		user = Admin.query.filter_by(uname = uname).first()
		if user and user.password == password:
				login_user(user)
				return redirect(url_for('admin_query'))
		else:
			return "Invalid Credentials"
	return render_template('admin_login.html')

#admin query
@app.route('/adminquery')
@login_required
def admin_query():
	return render_template('admin_query.html')

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
		return jsonify({'Add_Status':True,'Customer_Details':{'Username':user.uname,'Camper':user.camper_order}})

	return render_template('add_cust.html')


#customer details
@app.route('/customer_detail',methods=['GET','POST'])
@login_required
def cust_detail():
	if request.method=='POST':
		uname = request.form['uname']
		camp = request.form['camp']
		user = Customer.query.filter((Customer.uname == uname) | (Customer.camper_order == camp) )
		users_dict = {}
		# print(type(user))
		if user.count()==0:
			return "Null Records"
		x=1
		for users in user:
			u1 = {'Show_Status':True,'Customer_Details':{'Username':users.uname,'Camper':users.camper_order , 'tim_dliv':users.time_diliv}}
			users_dict["User"+str(x)]=u1
			x=x+1
		return jsonify(users_dict)

	return render_template('cust_detail.html')

# all cust

@app.route('/all_customer_detail',methods=['GET','POST'])
@login_required
def all_cust_detail():
	user = Customer.query.filter_by().all()
	users_dict = {}
	x=1
	for users in user:
		u1 = {'Show_Status':True,'Customer_Details':{'Username':users.uname,'Camper':users.camper_order , 'tim_dliv':users.time_diliv}}
		users_dict["User"+str(x)]=u1
		x=x+1
	return jsonify(users_dict)

	# return	 "hi"
		



# jsonify({'Login_Status':True,'Admin_Details':{'Username':user.uname,'Pass':user.password}})