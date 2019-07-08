from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)
wsgi_app = app.wsgi_app

@app.route('/register/', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		new_user = User(username=request.form['username'], password=request.form['password'])
		db.session.add(new_user)
		db.session.commit()
		return home()
	return render_template('login.html')



app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


