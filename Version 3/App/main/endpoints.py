from flask import render_template, redirect, url_for
from ..url_authenticater import redirect_back
from .setup import main, variables


def get_page(name):
    return variables['pages'.upper()].get(name)


def main_prefix(endpoint):
    return variables['prefix'.upper()] + endpoint


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
    template = get_page('home')
    return render_template(template, website_name=variables['WEBSITE_NAME'])
