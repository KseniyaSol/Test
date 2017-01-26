import requests
def inp():
    site = input('Enter site: ')
    return site
site = inp()
rect = requests.get(site)
print(rect.status_code)

#'http://httpbin.org/status/415' - example of input data