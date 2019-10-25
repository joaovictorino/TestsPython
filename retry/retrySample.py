import requests
from retry.api import retry_call

def make_trouble(service, info=None):
    if not info:
        info = ''
    r = requests.get(service + info)
    return r.text


def what_is_my_ip(approach=None):
    if approach == "optimistic":
        tries = 1
    elif approach == "conservative":
        tries = 3
    else:
        # skeptical
        tries = -1
    #result = retry_call(make_trouble, fargs=["http://ipinfo.io/"], fkwargs={"info": "ip"}, tries=tries)
    result = retry_call(make_trouble, fargs=["http://ipinfo.io/"], tries=tries)
    print(result)

what_is_my_ip("conservative")