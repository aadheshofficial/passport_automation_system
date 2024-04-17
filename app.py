
from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# from flask_wtf import wtforms
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "123"


db = SQLAlchemy(app)



class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(80),nullable=False)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=['POST', 'GET'])
def user_login():
    if request.method == 'POST':
        uname = request.form['user_login_username']
        passw = request.form['user_login_password']
        # print(uname)
        passw = bcrypt.generate_password_hash(passw)
        # return redirect(url_for("home"))
        new_user = User(username=uname,password=passw)
        db.session.add(new_user)
        db.session.commit()
        # return "helo world "+str(uname)
        return redirect("/")
    return render_template("user_login.html")



@app.route("/forget_password")
def forget_password():
    return render_template("forget_password_user_login.html")

@app.route("/register_user",methods=['POST', 'GET'])
def show_register_user_form():
    if request.method =='POST':
        name = request.form['new_user_register_name']
        aadharno = request.form['new_user_register_aadharnumber']
        phone = request.form['new_user_register_phone']
        email = request.form['new_user_register_email']
        adderss = request.form['new_user_register_address']
        fathername = request.form['new_user_register_fathersname']
        mothername = request.form['new_user_register_mothername']
        dob = request.form['new_user_register_dob']
        username = request.form['new_user_register_username']
        password = request.form['new_user_register_password']
        reenter = request.form['new_user_register_reenter']
        # return "register successful"
        return redirect("/")
    return render_template("register_user_login.html")

@app.route("/change_password")
def change_password():
    return render_template("change_password_user_login.html")
@app.route("/apply_passport",methods=['POST', 'GET'])
def apply_passport():
    if request.method =='POST':
        name = request.form['apply_passport_name']
        fathername = request.form['apply_passport_father_name']
        mothername = request.form['apply_passport_mother_name']
        dob = request.form['apply_passport_dob']
        phone = request.form['apply_passport_phone']
        adderss = request.form['apply_passport_adderss']
        email = request.form['apply_passport_email']
        select = request.form['apply_passport_id_proof']
        idprooffile = request.form['apply_passport_id_proof_file']
        mark10th = request.form['apply_passport_10th_mark_sheet'] 
        mark12th = request.form['apply_passport_12th_mark_sheet']
        pancard = request.form['apply_passport_pan_card']
        return redirect("/make_payment")
    return render_template("apply_passport.html")
@app.route("/user_profile")
def user_profile():
    return render_template("user_profile.html")
@app.route("/make_payment")
def make_payment():
    return render_template("make_payment.html")
@app.route("/status_result")
def status_result():
    return render_template("status_result.html")
@app.route("/check_status")
def check_status():
    return render_template("check_status.html")
if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)