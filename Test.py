import http.client
site = input("Введите сайт")
conn = http.client.HTTPConnection(site)
conn.request("GET", "/sandbox")
r1 = conn.getresponse()
print(r1.status)

data1 = r1.read()
conn.request("GET", "/companies/")
r2 = conn.getresponse()
print(r2.status)

data2 = r2.read()
conn.close()
input('Для продолжения нажмите [Enter] . . .')