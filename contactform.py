from flask import Flask,render_template,flash,redirect,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms_validators import AlphaSpace,Integer
from config import Config
from datetime import datetime
import pymysql
from flask_wtf.csrf import CsrfProtect
import smtplib

sender = 'harshit2772@gmail.com'
app = Flask(__name__)
app.config.from_object(Config)
app.config["DEBUG"] = True
CsrfProtect(app)

con = pymysql.connect('localhost','root','','contactinfo')
cur = con.cursor()

class LoginForm(FlaskForm):
		username = StringField('username',validators=[AlphaSpace(message = "Name should contain only alphabets and space")])
		mobile = StringField('mobile',validators=[Integer(),validators.Length(min=10, max=10,message = "Enter Valid Contact Number")])
		email = StringField('email')
		subject = StringField('subject')
		message = StringField('message')
		#submit = SubmitField('Submit')

@app.route('/')
def home():
	return render_template('contactinfo.html',flag = 0)

@app.route('/contactinfo', methods=['GET', 'POST'])
def contactinfo():
	form = LoginForm()
	if form.validate_on_submit():
		date = str(datetime.now())
		date_time = date[:16]
		try:
			cur.execute("insert into information(username,email,mobile_number,subject,message,Date_time) values(%s,%s,%s,%s,%s,%s)",(form.username.data,form.email.data,form.mobile.data,form.subject.data,form.message.data,date_time))
			con.commit()
			from email.mime.multipart import MIMEMultipart
			from email.mime.text import MIMEText
			me = "*******@gmail.com"
			my_password = "*******"
			you = form.email.data
			msg = MIMEMultipart('alternative')
			msg['Subject'] = "Regarding your feedback"
			msg['From'] = me
			msg['To'] = you
			html = '<html><body><p>Hello <strong>'+form.username.data+'</strong><br></p><br>Thank you so much for your valuable feedback!<p> We’re very happy that you loved the experience, and appreciate the time you took to send us a note or complete our survey. As a company, we strive to do our best to make customers happy and this motivates us to keep on improving! </p><br><br><p>Kind Regards,</p><p>Harshit Kumawat</P><p>Shramista Technologies, 9876543210</p></body></html>'
			part2 = MIMEText(html, 'html')
			msg.attach(part2)
			s = smtplib.SMTP_SSL('smtp.gmail.com')
			s.login(me, my_password)
			s.sendmail(me, you, msg.as_string())
			s.quit()
		except TypeError as e:
			return render_template('contactinfo.html',error=e,flag=0)

	return render_template('contactinfo.html',form = form,flag=1)

app.run()