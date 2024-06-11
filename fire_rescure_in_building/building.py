from flask import Flask,Blueprint,render_template,session,redirect,url_for,request,flash
from database import*
import uuid

building=Blueprint('building',__name__)


@building.route('/building_home')
def building_home():

	return render_template('building_home.html')

@building.route('/building_uploadfloorimage',methods=['post','get'])
def building_uploadfloorimage():
	data={}
	q="select * from image"
	res=select(q)
	data['img']=res

	if "add" in request.form:
		bid=session['building_id']
		i=request.files['imgg']
		path=path="static/image/"+str(uuid.uuid4())+i.filename
		i.save(path)
		q="insert into image values(null,'%s','%s')"%(bid,path)
		insert(q)
		flash('insert successfully')
		return redirect(url_for('building.building_uploadfloorimage'))
		
	return render_template('building_uploadfloorimage.html',data=data)	

@building.route('/building_sendfirerequest',methods=['post','get'])	
def building_sendfirerequest():
	data={}
	q="select * from request inner join building using (building_id)"
	res=select(q)
	data['req']=res

	if "request" in request.form:
		bid=session['building_id']
		d=request.form['des']
		da=request.form['date']
		t=request.form['time']
		q="insert into request values(null,'%s','%s','%s','%s','pending')"%(bid,d,da,t)
		insert(q)
		flash('insert successfully')
		return redirect(url_for('building.building_sendfirerequest'))

		
	return render_template('building_sendfirerequest.html',data=data)

@building.route('/building_viewpositions')	
def building_viewpositions():
	data={}
	rid=request.args['rid']
	q="select * from `position` inner join officers using (officer_id) inner join request using(request_id) where request_id='%s'"%(rid)
	res=select(q)
	data['pos']=res

	return render_template('building_viewpositions.html',data=data)