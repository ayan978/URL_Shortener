from flask import Blueprint, render_template

short = Blueprint('short', __name__)

@short.route('/<shortened_url>')
def redirect_to_url(shortened_url):
    pass

@short.route('/')
def index():
    return render_template('index.html')

@short.route('/add_link', methods=['POST'])
def add_link():
    pass

@short.route('/stats')
def stats():
    pass

@short.errorhandler(404)
def page_not_found(e):
    return '', 404