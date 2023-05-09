from flask import render_template

from . import bp

@bp.route('/')
def home():
    return render_template('index.jinja', title='Home')

@bp.route('/images')
def images():
    return render_template('images.jinja', title='Images')

@bp.route('/locations')
def locations():
    return render_template('locations.jinja', title='Locations')

@bp.route('/certs')
def certs():
    return render_template('certs.jinja', title='Certifications')