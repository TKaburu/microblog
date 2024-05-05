from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Tracey'}
    return render_template ('home.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Requested for user{}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', form=form)