# This file and all the others are dictated to our community project of myp 4.

# How to create blueprints and setup the application:
# https://www.youtube.com/watch?v=pjVhrIJFUEs
# https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints

# How to create an Application factory and setup the application:
# https://www.youtube.com/watch?v=Wfx4YBzg16s&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=11
# https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/#app-factories

# How to create a production ready web server:
# https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/#gunicorn

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
        "LAUNCH": launch_start
    }

    from .main import main
    from .posts import post
    from .info_pages import info

    app.register_blueprint(main)
    app.register_blueprint(post)
    app.register_blueprint(info)

    @app.route('/')
    def root():
        return 'home page'

    return app, app_variables


def deploy_production(app, variables):
    print('http://192.168.0.129:8080', 'http://127.0.0.1:8080/', )

    from gevent.pywsgi import WSGIServer

    http_server = WSGIServer(
        (variables.get('host'.upper()), variables.get('port'.upper())),
        app
    )
    http_server.serve_forever()


def deploy_test(app, variables, debug=True):
    app.run(
        debug=debug,
        host=variables.get('host'.upper()),
        port=variables.get('port'.upper())
    )


def run_app(debug=True):
    app, variables = create_app()
    launch_speed = round(time.time() - variables['launch'.upper()], 3)
    print(f'The app was lunched with a {launch_speed} second execution.')

    deploy_test(app, variables)

