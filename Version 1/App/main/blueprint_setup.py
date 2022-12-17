from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/main', static_folder='static', template_folder='templates')


def new_page(name):
    # page_prefix: 'main/'
    return f'main/{name}.html'


main_variables = {
    'PAGES': {
        'Home': new_page('home')
    },
    'PREFIX': 'main.'
}

