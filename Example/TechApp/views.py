from TechApp import app
from flask import render_template, redirect, url_for, request

@app.route('/') 
@app.route('/home')
def homepage():
	return render_template('index.html')

