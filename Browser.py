import requests


def choice(url):
    print('Choice your protocol http or https')
    prot = str(input('Enter protocol: '))
    site_ = prot+'://'+str(url)
    return site_


def inp(method, conn):
    if method == 'input':
        ex = ['ex.org']
        print('Example of input data: '+ex[0])
        site_ = input(str('Enter site: '))         # httpbin.org/status/415 - example of input data
        return site_
    elif method == 'headers':
        headers_ = conn.headers
        return headers_
    elif method == 'code':
        code_ = conn.status_code
        return code_


def print_headers(head):
    for key, value in head.items():
        print(key, ': ', value)
rect = ''
site = inp('input', rect)
site = choice(site)
rect = requests.get(site, allow_redirects=False)
headers = inp('headers', rect)
print('Headers of '+str(site)+' are: ')
print_headers(headers)
code = inp('code', rect)
print(str(code)+' '+rect.reason)