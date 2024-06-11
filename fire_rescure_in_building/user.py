from flask import Flask,Blueprint,render_template 
from database import*

user=Blueprint('user',__name__)

@user.route('user_home')
def user_home():
	return render_template('user_home.html')

@user.route('user_viewfire')	
def user_viewfire():
	data={}
	q="select * from request inner join building using (building_id)"
	res=select(q)
	data['req']=res

	return render_template('user_viewfire.html',data=data)

@user.route('user_viewbuilding')	
def user_viewbuilding():
	data={}
	q="select * from building"
	res=select(q)
	data['bu']=res

	return render_template('user_viewbuilding.html',data=data)
@user.route('user_viewimage')	
def user_viewimage():
	data={}
	q="select * from image"
	res=select(q)
	data['img']=res

	return render_template('user_viewimage.html',data=data)