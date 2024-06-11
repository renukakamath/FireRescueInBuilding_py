from flask import Flask 
from public import public
from admin import admin
from building import building
from user import user
from fire import fire


app=Flask(__name__)

app.secret_key='key'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(building,url_prefix='/building')
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(fire,url_prefix='/fire')



app.run(debug=True,port=5035)