from flask import render_template, redirect, url_for
from ..url_authenticater import redirect_back, add_prefix
from .blueprint_setup import post, post_variables


def get_page(name):
    return post_variables['PAGES'].get(name)


def post_prefix(endpoint):
    return add_prefix(endpoint, post_variables['prefix'.upper()])


@post.route('/')
def root():
    redirect_url = url_for(
        post_prefix('home')
    )
    redirect_back_endpoint = post_prefix('secure')
    return redirect(redirect_back(redirect_url, redirect_back_endpoint))


@post.route('/secure')
def secure():
    return ''


@post.route('/Home')
def home():
    route_template = get_page('Home')
    return render_template(route_template)
