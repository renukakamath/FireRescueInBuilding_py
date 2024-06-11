from flask import Flask,Blueprint,render_template,request,redirect,url_for,session,flash 
from database import*

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('public_home.html')

@public.route('/user_registration',methods=['post','get'])
def user_registration():
	if "ureg" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		pl=request.form['place']
		ph=request.form['phno']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			flash('already exist')
		else:
			q="insert into login values(null,'%s','%s','user')"%(u,pa)
			id=insert(q)
			q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,f,l,pl,ph,e)
			insert(q)
			flash('insert successfully')
			return redirect(url_for('public.user_registration'))
	return render_template('user_registration.html')


@public.route('/fire_registration',methods=['post','get'])	
def fire_registration():
	if "freg" in request.form:
		fn=request.form['fname']
		la=request.form['lname']
		pl=request.form['pla']
		nu=request.form['num']
		em=request.form['email']
		
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			flash('already exist')
		else:
			q="insert into login values(null,'%s','%s','officer')"%(u,pa)
			id=insert(q)
			q="insert into officers values(null,'%s','%s','%s','%s','%s','%s')"%(id,fn,la,pl,nu,em)
			insert(q)
			print(q)
			flash('insert successfully')
			return redirect(url_for('public.fire_registration'))

		
	return render_template('fire_registration.html')

@public.route('/building_registration',methods=['post','get'])	
def building_registration():
	if "breg" in request.form:
		fn=request.form['fname']
	
		pl=request.form['pla']
		nu=request.form['num']
		em=request.form['email']
		la=request.form['lat']
		lo=request.form['lon']
		
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			flash('already exist')
		else:
			q="insert into login values(null,'%s','%s','owner')"%(u,pa)
			id=insert(q)
			q="insert into building values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fn,pl,nu,em,la,lo)
			insert(q)
			flash('insert successfully')
			return redirect(url_for('public.building_registration'))
			
	return render_template('building_registration.html')

@public.route('/login',methods=['post','get'])	
def login():
	if "login" in request.form:
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			lid=session['login_id']
			if res[0]['type']=="admin":
				return redirect(url_for('admin.admin_home'))

			elif res[0]['type']=="owner":
				q="select * from building where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['building_id']=res[0]['building_id']
					bid=session['building_id']

				return redirect(url_for('building.building_home'))

			elif res[0]['type']=="officer":
				q="select * from officers where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['officer_id']=res[0]['officer_id']
					oid=session['officer_id']

				return redirect(url_for('fire.fire_home'))

			elif res[0]['type']=="user":
				return redirect(url_for('user.user_home'))
				

		
	return render_template('login.html')

	


