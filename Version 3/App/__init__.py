# This file and all the others are dictated to our community project of myp 4.

# How to create blueprints and setup the application:
# https://www.youtube.com/watch?v=pjVhrIJFUEs
# https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints
# https://flask.palletsprojects.com/en/2.2.x/blueprints/

# How to create an Application factory and setup the application:
# https://www.youtube.com/watch?v=Wfx4YBzg16s&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=11
# https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/#app-factories

# How to create a production ready web server:
# https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/#gunicorn

# How to create and manage exceptions:
# https://www.programiz.com/python-programming/user-defined-exception
# https://www.w3schools.com/python/gloss_python_raise.asp

# -------------------------------------------------------------------------- #
# Imports
import time

from flask import Flask, redirect, url_for

from .config import Config

# -------------------------------------------------------------------------- #
launch_start = time.time()


# -------------------------------------------------------------------------- #

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    app_variables = {
        "PORT": 8080,
        "HOST": "0.0.0.0",
        "LAUNCH": {'start': launch_start}
    }

    from .main import main
    from .posts import post
    from .info_pages import info

    app.register_blueprint(main)
    app.register_blueprint(post)
    app.register_blueprint(info)

    @app.route('/')
    def root():
        return redirect(url_for('main.root'))

    return app, app_variables

# -------------------------------------------------------------------------- #
# Deploy options:
# deploy production --> production ready website | complete website
# deploy test --> website being tested and built | not ready for production deployment


# deploy_option: PRODUCTION
def deploy_production(app, variables, action=None):
    if action is not None:
        exec(action)

    print('http://192.168.0.129:8080', 'http://127.0.0.1:8080/', )

    from gevent.pywsgi import WSGIServer

    http_server = WSGIServer(
        (variables.get('host'.upper()), variables.get('port'.upper())),
        app
    )
    http_server.serve_forever()


# deploy_option: TEST
def deploy_test(app, variables, action=None, debug=True):
    if action is not None:
        exec(action)

    app.run(
        debug=debug,
        host=variables.get('host'.upper()),
        port=variables.get('port'.upper())
    )


ID_CODE = {'PRODUCTION': deploy_production, 'TEST': deploy_test}


class InvalidDeploymentRequest(Exception):
    """Raised when the deployment request is not in the ID_CODE deployment list

    Attributes:
        deploy_option - - input deployment option which caused the error
        message - - explanation of the error

    """

    def __init__(self, deploy_option, message="** Invalid request for deployment **"):
        self.deploy_option = deploy_option
        self.message = message
        super().__init__(self.message)

# -------------------------------------------------------------------------- #


def run_app(debug=True, deploy_option='TEST'):
    """deploy_option: PRODUCTION: deploy_production | TEST: deploy_test"""

    app, variables = create_app()

    variables['LAUNCH']['end'] = time.time()
    variables['LAUNCH']['speed'] = round(variables['LAUNCH']['start'] - variables['LAUNCH']['end'], 3)

    try:
        if ID_CODE.get(deploy_option) is None:
            raise InvalidDeploymentRequest(deploy_option)
        else:
            ID_CODE.get(deploy_option)(
                app, variables,
                action=str(
                    print(f"The app was lunched with a {variables['LAUNCH']['speed']} second execution.")),
                debug=debug
            )

    except TypeError:
        ID_CODE.get(deploy_option)(
            app, variables,
            action=str(
                print(f"The app was lunched with a {variables['LAUNCH']['speed']} second execution.")),
        )

