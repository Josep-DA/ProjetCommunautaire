from flask import Blueprint

info = Blueprint('info', __name__, url_prefix='/info', static_folder='static', template_folder='templates')


def new_page(name):
    # page_prefix: 'info/'
    return f'info/{name}.html'


info_variables = {
    'PAGES': {
        'Home': new_page('home')
    },
    'PREFIX': 'info.'
}
