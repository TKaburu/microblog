from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Tracey'}
    return render_template ('home.html', user=user)