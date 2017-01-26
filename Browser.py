import requests


def inp(method):
    if method == 'input':
        ex = ['http://ex.org/']
        corr = False
        while (corr == False):
            print('Example of input data: '+ex[0])
            site = input('Enter site: ')         # 'http://httpbin.org/status/415' - example of input data
            if site.find('http://') > -1:
                corr = True
                return site
            else:
                print('Input isnt correct!')
    elif method == 'headers':
        headers = rect.headers
        return headers
    elif method == 'code':
        code = rect.status_code
        return code
site = inp('input')
rect = requests.get(site)
headers = inp('headers')
print('Headers of '+str(site)+' is '+str(headers))
code = inp('code')
print(str(code)+' '+rect.reason)