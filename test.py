


import requests

proxy = {"https": "http://user_6ca446:dfb877@portal.anyip.io:1080"}

res = requests.get("https://httpbin.org/ip", proxies=proxy)

print(res.text)