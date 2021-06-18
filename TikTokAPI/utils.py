import random
import string
import requests
import json


def random_key(length):
    key = ''
    for i in range(length):
        key += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    return key


def build_get_url(base_url, params, append=False):
    final_url = base_url
    if append:
        final_url += "&"
    else:
        final_url += "?"
    for key, val in params.items():
        final_url += key + "=" + val + "&"
    final_url = final_url[:-1]
    return final_url


def get_req_json(url, params=None, headers=None, proxy_endpoint=None):
    proxies = {'http': 'http://{}'.format(proxy_endpoint), 'https': 'https://{}'.format(proxy_endpoint)} if proxy_endpoint else None
    headers["Host"] = url.split("/")[2]
    r = requests.get(url, params=params, headers=headers, proxies=proxies)
    return json.loads(r.text)


def get_req_content(url, params=None, headers=None, proxy_endpoint=None):
    proxies = {'http': 'http://{}'.format(proxy_endpoint), 'https': 'https://{}'.format(proxy_endpoint)} if proxy_endpoint else None
    headers["Host"] = url.split("/")[2]
    r = requests.get(url, params=params, headers=headers, proxies=proxies)
    return r.content


def get_req_text(url, params=None, headers=None, proxy_endpoint=None):
    proxies = {'http': 'http://{}'.format(proxy_endpoint), 'https': 'https://{}'.format(proxy_endpoint)} if proxy_endpoint else None
    headers["Host"] = url.split("/")[2]
    r = requests.get(url, params=params, headers=headers, proxies=proxies)
    return r.text


def python_list2_web_list(data):
    web_list = "[\""
    web_list += '", "'.join(data)
    web_list += "\"]"
    return web_list
