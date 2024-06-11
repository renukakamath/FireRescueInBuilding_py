from flask import Flask,Blueprint,render_template,request,session,redirect,url_for,flash 
from database import*

fire=Blueprint('fire',__name__)

@fire.route('/fire_home')
def fire_home():

	return render_template('fire_home.html')

@fire.route('/fire_viewrequest')
def fire_viewrequest():
	data={}
	q="select * from request inner join building using (building_id)"
	res=select(q)
	data['req']=res

	if "action" in request.args:
		action=request.args['action']
		bid=request.args['bid']
	else:
		action=None
	if action=='accept':
		q="update  request set status='accept' where building_id='%s'"%(bid)
		update(q)

	if action=='reject':
		q="update request set status='reject' where building_id='%s'"%(bid)
		update(q)
					


	return render_template('fire_viewrequest.html',data=data)
@fire.route('/fire_viewbuildings')
def fire_viewbuildings():
	data={}
	q="select * from building"
	res=select(q)
	data['own']=res

	return render_template('fire_viewbuildings.html',data=data)

@fire.route('/fire_viewimage')	
def fire_viewimage():
	data={}
	q="select * from image"
	res=select(q)
	data['img']=res

	return render_template('fire_viewimage.html',data=data)

@fire.route('/fire_addposition',methods=['post','get'])	
def fire_addposition():

	data={}
	q="select * from request inner join building using (building_id)"
	res=select(q)
	data['requ']=res

	if "position" in request.form:
		oid=session['officer_id']
		r=request.form['req']
		d=request.form['det']
		q="insert into position values(null,'%s','%s','%s')"%(oid,r,d)
		insert(q)
		flash('insert successfully')
		return redirect(url_for('fire.fire_addposition'))
	

	return render_template('fire_addposition.html',data=data)

@fire.route('/fire_viewofficerandposition')
def fire_viewofficerandposition():
	data={}
	q="select * from position inner join officers using (officer_id) inner join request using (request_id)"
	res=select(q)
	data['pos']=res

	return render_template('fire_viewofficerandposition.html',data=data)	

@fire.route('/fire_sendemergency',methods=['post','get'])	
def fire_sendemergency():
	data={}
	q="select * from request inner join building using(building_id) "
	res=select(q)
	data['reqs']=res

	if "details" in request.form:
		oid=session['officer_id']
		r=request.form['req']
		d=request.form['det']
		q=" insert into emergency values (null,'%s','%s','%s')"%(r,oid,d)
		insert(q)
		flash('insert successfully')
		return redirect(url_for('fire.fire_sendemergency'))
		
	return render_template('fire_sendemergency.html',data=data)
	