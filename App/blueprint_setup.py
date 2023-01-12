from flask import Blueprint

# -------------------------------------------------------------------------- #


def create_main(name: str):
    bp = Blueprint(
        name, __name__, url_prefix=f'/{name}',
        static_folder=f'{name}/static/{name}/', template_folder=f'{name}/templates')

    variables = {
        'PAGES': {
            # page_prefix: 'main/'
            'home': f'{name}/home.html'
        },
        'PREFIX': f'{name}.',
        'WEBSITE_NAME': 'LA POLY. VERTE'
    }

    return bp, variables

