from urllib.parse import urlparse, urljoin
from flask import request, url_for

# Lien pour la documentation:
# Vérification des redirections: 'https://web.archive.org/web/20120517003641/http://flask.pocoo.org/snippets/62/'
# Pour créer des fonction de décoration: 'https://realpython.com/primer-on-python-decorators/

Accepted_endpoints = (
    'https://Projet-communautaire-Code--jadleonard.repl.co'
    
    'https://Projet-communautaire-Code--jadleonard.repl.co/main/secure',
    'https://Projet-communautaire-Code--jadleonard.repl.co/main/Home',

    'https://Projet-communautaire-Code--jadleonard.repl.co/post/secure',
    'https://Projet-communautaire-Code--jadleonard.repl.co/post/Home',

    'https://Projet-communautaire-Code--jadleonard.repl.co/info/secure',
    'https://Projet-communautaire-Code--jadleonard.repl.co/info/Home'

)


# Cette fonction est pour vérifier si l'url de redirection est un url appartenant à notre serveur.
def is_url_safe(target):
    host_url = request.host_url
    print(host_url)
    if host_url != 'https://Projet-communautaire-Code--jadleonard.repl.co':
        host_url = 'https://Projet-communautaire-Code--jadleonard.repl.co'
    reference_url = urlparse(host_url)
    test_http_link = urljoin(host_url, target)
    test_url = urlparse(test_http_link)
    
    print(test_url.scheme in ('http', 'https'))
    print(reference_url.netloc == test_url.netloc)
    print(test_http_link in Accepted_endpoints)
    
    return test_url.scheme in ('http', 'https') and reference_url.netloc == test_url.netloc and test_http_link in Accepted_endpoints


# Cette fonction permet de rediriger les utilisateurssi jamais l'url s'avère à ne pas appartenir à notre serveur.
# Cette une fonction dite "fallback" -> "plan de secours".
def redirect_back(target, endpoint, **values):
    if not is_url_safe(target):
        print('ho no!')
        target = url_for(endpoint, **values)
    return target


def add_prefix(endpoint, bp_prefix):
    func_to_get = bp_prefix + endpoint
    return func_to_get

