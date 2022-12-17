from flask import Blueprint

# -------------------------------------------------------------------------- #


def create_main():
    main = Blueprint(
        'main', __name__, url_prefix='/main',
        static_folder='main/static/main/', template_folder='main/templates')

    main_variables = {
        'PAGES': {
            # page_prefix: 'main/'
            'home': 'main/home.html'
        },
        'PREFIX': f'main.',
        'WEBSITE_NAME': 'LA POLY. VERTE'
    }

    return main, main_variables

