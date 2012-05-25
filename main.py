import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#  Routing for the stats application

@app.route('/')
def home():
	"""Render website's home page."""
	return render_template('index.html')


#  Functions below can be used for all Flask apps

@app.errorhandler(404)
def page_not_found(error):
	"""Custom 404 page."""
	return render_template('404.html')

	
if __name__ == '__main__':
	app.run(debug=True)