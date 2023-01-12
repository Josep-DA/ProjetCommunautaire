from flask import Blueprint

post = Blueprint('post', __name__, url_prefix='/main', static_folder='static', template_folder='templates')


def new_page(name):
    # page_prefix: 'post/'
    return f'post/{name}.html'


post_variables = {
    'PAGES': {
        'Home': new_page('home')
    },
    'PREFIX': 'post.'
}

