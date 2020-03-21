from app import app
from app import db
from flask import render_template, flash , redirect, url_for
from app.form import LoginForm,RegistrationForm
from app.models import User
from flask_login import current_user, login_user , logout_user, login_required
from app.prahaApi import getcurrentInfo

#routing for index page
@app.route("/")
@app.route("/index")
@login_required
def index():
    posts = [


        {
            'autor':{'username': 'John'},
            'body': "test1"
        },
        {
            'autor':{'username':'Susan'},
            'body':'test2'

        }
    ]
    return render_template('index.html', title ="HomePage",posts = posts)

#routing for login page
#you add to define your login function after your route
@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',title="Sign In",form = form)


@app.route('/logout')
def logout():
    logout_user()
    flash("you are now logout")
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    registerForm = RegistrationForm()
    if registerForm.validate_on_submit():
        user = User(username=registerForm.username.data,email=registerForm.email.data)
        user.set_password(registerForm.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now register")
        return redirect(url_for('login'))

    return render_template('register.html',title = "Register",form = registerForm)

@app.route('/testAPI',methods = ['GET','POST'])
def testAPI():
    api = getcurrentInfo()
    print(type(api))
    return render_template('testAPI.html',title="testAPI", element = api)


@app.route('/background_process_test')
def background_process_test():
    updateAPI = getcurrentInfo()
    updateAPI_string = str(updateAPI)
    return updateAPI_string


