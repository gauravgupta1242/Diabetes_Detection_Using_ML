from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
# import created database from tabledef.py

from tabledef import *
engine = create_engine('sqlite:///register.db', echo=True)


app = Flask(__name__)
wsgi_app = app.wsgi_app 
# CHECK session login or not
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return  "Hello ,"+"   " +  str(request.form['username'])+ render_template('homepage.html') 

# login page and take userword and password
@app.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

# home page registration button 
@app.route('/register_button/', methods=['GET','POST'])
def register():
        return render_template('registered.html') 




# registration page 
@app.route('/reg_page/', methods=['GET', 'POST'])
def registered_page():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    POST_MAIL_ID = str(request.form['mail_id'])
    POST_PHONE_NUMBER = str(request.form['phone_number'])
    Session = sessionmaker(bind=engine)
    session = Session()
    xyz = User( POST_USERNAME , POST_PASSWORD,POST_MAIL_ID,POST_PHONE_NUMBER)
    session.add(xyz)
    session.commit()
    return render_template('registration.html') + "   <a href='/logout'>LOG IN </a>"
      
# back to dashboard button on medical report
@app.route('/back_to_dashboard/')
def back_to_dashboard():
    return render_template('homepage.html')

# medical page registration button 
@app.route('/medical_button/', methods=['GET','POST'])
def medical():
        return render_template('medical_detail.html') 


  
# medical detail
@app.route('/medical_detail/', methods=['GET', 'POST'])
def mediacal_detail():
    BLOOD_PRESSURE = str(request.form['blood_pressure'])
    INSULINE = str(request.form['insuline'])
    BMI = str(request.form['bmi'])
    DPF = str(request.form['dpf'])
    AGE = str(request.form['age'])
    Session = sessionmaker(bind=engine)
    session = Session()
    xy = abc(BLOOD_PRESSURE,INSULINE,BMI,DPF,AGE)
    session.add(xy)
    session.commit()
    return render_template('medical_input.html')  + "   <a href='/back_to_dashboard/'>Back to dashboard </a>"


# past report page registration button 
@app.route('/past_report_button/', methods=['GET','POST'])
def past():
        return render_template('past_report.html')


# logout
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


 
if __name__ == "__main__":
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)