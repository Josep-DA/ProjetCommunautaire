from urllib.parse import urlparse, urljoin
from flask import request, url_for, redirect

# Lien pour la documentation:
# Vérification des redirections: 'https://web.archive.org/web/20120517003641/http://flask.pocoo.org/snippets/62/'
# Pour créer des fonction de décoration: 'https://realpython.com/primer-on-python-decorators/

Accepted_endpoints = (
    'http://192.168.0.129:8080', 'http://127.0.0.1:8080/',
    'http://192.168.0.129:8080/main/secure', 'http://127.0.0.1:8080/main/secure',
    'http://192.168.0.129:8080/main/Home', 'http://127.0.0.1:8080/main/Home',

    'http://192.168.0.129:8080/post/secure', 'http://127.0.0.1:8080/post/secure',
    'http://192.168.0.129:8080/post/Home', 'http://127.0.0.1:8080/post/Home',

    'http://192.168.0.129:8080/info/secure', 'http://127.0.0.1:8080/info/secure',
    'http://192.168.0.129:8080/info/Home', 'http://127.0.0.1:8080/info/Home',

)


# Cette fonction est pour vérifier si l'url de redirection est un url appartenant à notre serveur.
def is_url_safe(target):
    reference_url = urlparse(request.host_url)
    test_http_link = urljoin(request.host_url, target)
    test_url = urlparse(test_http_link)
    return test_url.scheme in ('http', 'https') and reference_url.netloc == test_url.netloc and \
           test_http_link in Accepted_endpoints


# Cette fonction permet de rediriger les utilisateurssi jamais l'url s'avère à ne pas appartenir à notre serveur.
# Cette une fonction dite "fallback" -> "plan de secours".
def redirect_back(target, endpoint, **values):
    if not is_url_safe(target):
        target = url_for(endpoint, **values)
    return target


def add_prefix(endpoint, bp_prefix):
    func_to_get = bp_prefix + endpoint
    return func_to_get

