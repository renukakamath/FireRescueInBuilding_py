from flask import Flask,Blueprint,render_template,request 
from database import*

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

	return render_template('admin_home.html')
@admin.route('/admin_viewbuilding')	
def admin_viewbuilding():
	data={}
	q="select * from building"
	res=select(q)
	data['own']=res

	return render_template('admin_viewbuilding.html',data=data)

@admin.route('/admin_viewimage')	
def admin_viewimage():
	data={}

	q="select * from image"
	res=select(q)
	data['img']=res

	return render_template('admin_viewimage.html',data=data)
@admin.route('/admin_viewfireofficer')	
def admin_viewfireofficer():
	data={}
	q="select * from officers"
	res=select(q)
	data['off']=res
	return render_template('admin_viewfireofficer.html',data=data)

@admin.route('/admin_viewuser')	
def admin_viewuser():
	data={}
	q="select * from user"
	res=select(q)
	data['use']=res

	return render_template('admin_viewuser.html',data=data)

@admin.route('/admin_viewfirerequest')
def admin_viewfirerequest():
	data={}
	q="select * from request inner join building using(building_id)"
	res=select(q)
	data['req']=res
	
	return render_template('admin_viewfirerequest.html',data=data)	

@admin.route('/admin_viewposition')	
def admin_viewposition():
	data={}
	q="select * from `position` inner join officers using (officer_id) inner join request using(request_id)"
	res=select(q)
	data['pos']=res

	return render_template('admin_viewposition.html',data=data)

@admin.route('/admin_viewbuildings')
def admin_viewbuildings():
	data={}
	bid=request.args['bid']
	q="select * from building where building_id='%s'"%(bid)
	res=select(q)
	data['bu']=res
	return render_template('admin_viewbuildings.html',data=data)
