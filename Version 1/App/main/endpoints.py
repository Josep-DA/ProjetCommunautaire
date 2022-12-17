from flask import render_template, redirect, url_for
from ..url_authenticater import redirect_back, add_prefix
from .blueprint_setup import main, main_variables


def get_page(name):
    return main_variables['pages'.upper()].get(name)


def main_prefix(endpoint):
    return add_prefix(endpoint, main_variables['prefix'.upper()])


@main.route('/')
def root():
    redirect_url = url_for(
        main_prefix('home')
    )
    redirect_back_endpoint = main_prefix('secure')
    return redirect(redirect_back(redirect_url, redirect_back_endpoint))


@main.route('/secure')
def secure():
    return ''


@main.route('/Home')
def home():
    route_template = get_page('Home')
    return render_template(route_template)
