from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from flask_migrate import Migrate
from flask_login import current_user
from flask import g
from flask_login import current_user
from flask_login import login_required
import json

# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='Secret key'


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/'add your db name'
db=SQLAlchemy(app)
migrate = Migrate(app, db)

# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Department(db.Model):
    cid=db.Column(db.Integer,primary_key=True)
    branch=db.Column(db.String(100))

class Attendence(db.Model):
    aid=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(100))
    attendance=db.Column(db.Integer())

class Trig(db.Model):
    tid=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(100))
    action=db.Column(db.String(100))
    timestamp=db.Column(db.String(100))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))





class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    rollno=db.Column(db.String(50))
    sname=db.Column(db.String(50))
    sem=db.Column(db.Integer)
    gender=db.Column(db.String(50))
    branch=db.Column(db.String(50))
    email=db.Column(db.String(50))
    number=db.Column(db.String(12))
    address=db.Column(db.String(100))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/studentdetails')
@login_required
def studentdetails():
    # Query the Student table using SQLAlchemy ORM
    students = Student.query.all()
    return render_template('studentdetails.html', students=students)

@app.route('/triggers')
@login_required
def triggers():
    # Query the Trig table using SQLAlchemy ORM
    triggers = Trig.query.all()
    return render_template('triggers.html', triggers=triggers)

@app.route('/department', methods=['POST', 'GET'])
@login_required
def department():
    if request.method == "POST":
        dept = request.form.get('dept')
        query = Department.query.filter_by(branch=dept).first()
        if query:
            flash("Department Already Exist", "warning")
            return redirect('/department')
        dep = Department(branch=dept)
        db.session.add(dep)  # Add the new Department object to the session
        db.session.commit()  # Commit the changes to the database
        flash("Department Added", "success")
    return render_template('department.html')

@app.route('/addattendance', methods=['POST', 'GET'])
@login_required
def addattendance():
    # Query the Student table using SQLAlchemy ORM
    students = Student.query.all()

    if request.method == "POST":
        rollno = request.form.get('rollno')
        attend = request.form.get('attend')
        
        # Check if both roll number and attendance are provided
        if not all([rollno, attend]):
            flash("Roll number and attendance are required fields!", "danger")
            return redirect(url_for('addattendance'))
        
        # Create a new Attendence object and add it to the session
        atte = Attendence(rollno=rollno, attendance=attend)
        db.session.add(atte)
        db.session.commit()
        flash("Attendance added", "warning")

    return render_template('attendance.html', students=students)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == "POST":
        rollno = request.form.get('roll')
        bio = Student.query.filter_by(rollno=rollno).first()
        attend = Attendence.query.filter_by(rollno=rollno).order_by(Attendence.aid.desc()).first()
        if bio:
            if attend:
                return render_template('search.html', bio=bio, attend=attend)
            else:
                return render_template('search.html', bio=bio, attend=None)
        else:
            flash("No student found with the provided roll number.", "danger")
    return render_template('search.html')
@app.route("/delete/<string:id>", methods=['POST', 'GET'])
@login_required

def delete(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        flash("Student Deleted Successfully", "success")
    else:
        flash("Student not found", "danger")
    return redirect('/studentdetails')


@app.route("/edit/<string:id>", methods=['POST', 'GET'])
@login_required
def edit(id):
    # Query the Department table using SQLAlchemy ORM
    departments = Department.query.all()
    posts = Student.query.filter_by(id=id).first()
    if request.method == "POST":
        rollno = request.form.get('rollno')
        sname = request.form.get('sname')
        sem = request.form.get('sem')
        gender = request.form.get('gender')
        branch = request.form.get('branch')
        email = request.form.get('email')
        num = request.form.get('num')
        address = request.form.get('address')

        # Update the student record using SQLAlchemy ORM
        posts.rollno = rollno
        posts.sname = sname
        posts.sem = sem
        posts.gender = gender
        posts.branch = branch
        posts.email = email
        posts.number = num
        posts.address = address
        db.session.commit()

        flash("Slot is Updated", "success")
        return redirect('/studentdetails')

    return render_template('edit.html', posts=posts, departments=departments)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist", "warning")
            return render_template('/signup.html')
        encpassword = generate_password_hash(password)

        # Insert the new user into the database using db.session.execute
        new_user = User(username=username, email=email, password=encpassword)
        db.session.add(new_user)
        db.session.commit()

        flash("Signup Success Please Login", "success")
        return render_template('login.html')

    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')    

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))



from flask import request

@app.route('/addstudent', methods=['POST', 'GET'])
@login_required
def addstudent():
    # Query the Department table using SQLAlchemy ORM
    dept = Department.query.all()

    if request.method == "POST":
        rollno = request.form.get('rollno')
        sname = request.form.get('sname')
        sem = request.form.get('sem')
        gender = request.form.get('gender')
        branch = request.form.get('branch')
        email = request.form.get('email')
        num = request.form.get('num')
        address = request.form.get('address')

        # Check if all fields are filled
        if not all([rollno, sname, sem, gender, branch, email, num, address]):
            flash("All fields are required!", "danger")
            return redirect(url_for('addstudent'))

        # Insert the new student into the database using SQLAlchemy ORM
        new_student = Student(rollno=rollno, sname=sname, sem=sem, gender=gender, branch=branch, email=email, number=num, address=address)
        db.session.add(new_student)
        db.session.commit()

        flash("Booking Confirmed", "info")
        return redirect(url_for('addstudent'))
    return render_template('student.html', dept=dept)


@app.route('/about')
def about():
    return render_template('about.html', user=current_user)

@app.before_request
def load_user():
    g.user = current_user

@app.context_processor
def inject_user():
    return dict(user=current_user)
@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        contact = Contact(name=name, email=email, message=message)
        db.session.add(contact)
        db.session.commit()
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)   