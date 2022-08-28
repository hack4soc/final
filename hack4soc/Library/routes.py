from flask_login import login_user, current_user, logout_user, login_required
from Library import app
from flask import render_template, redirect, url_for, flash
from Library import db
from Library.forms import LoginForm, RegistrationForm
from Library.models import User, book_table
from random import randint


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/register', methods = ['POST','GET'])
def register():
    lower, upper = 1, 34
    ans = randint(lower, upper)

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username =form.username.data, recent=ans)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login1'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error : {err_msg}", category='danger')
    
    return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login1():    
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user is not None and attempted_user.check_password(form.password.data):
            login_user(attempted_user)
            #flash(f"Success! You are logged in as : {attempted_user.username}", category="success")
            return redirect( url_for('dashboard_display'))      
            
        else:
            flash(f"Username and Password are not matching ! Please check again !", category="danger")
        
    return render_template("login.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout_function():
    logout_user()
    return redirect(url_for('login1'))

@app.route('/refresh')
@login_required
def fresh_refresh():    
    return redirect( url_for('dashboard_display'))

@app.route('/prof')
def prof_display():
    return render_template("profile.html")

@app.route('/his')
def hist_display():
    return render_template("history.html")

@app.route('/dashboarddisplay', methods=['GET', 'POST'])
def dashboard_display():
    book = book_table.query.filter_by(id = current_user.recent).first()    
    return render_template('dashboard.html', book=book)


# @app.route("/displaybook", methods=['GET', "POST"])
# def book_display():


