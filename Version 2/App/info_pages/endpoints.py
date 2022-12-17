from flask import render_template, redirect, url_for
from ..url_authenticater import redirect_back, add_prefix
from .blueprint_setup import info, info_variables


def get_page(name):
    return info_variables['PAGES'].get(name)


def info_prefix(endpoint):
    return add_prefix(endpoint, info_variables['prefix'.upper()])


@info.route('/')
def root():
    redirect_url = url_for(
        info_prefix('home')
    )
    redirect_back_endpoint = info_prefix('secure')
    return redirect(redirect_back(redirect_url, redirect_back_endpoint))


@info.route('/secure')
def secure():
    return ''


@info.route('/Home')
def home():
    route_template = get_page('Home')
    return render_template(route_template)
