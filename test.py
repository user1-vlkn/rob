


# import requests

# # proxy = {"https": "http://user_6ca446:dfb877@portal.anyip.io:1080"}
# proxy = {"https": "http://191.96.42.80:8080"}

# res = requests.get("https://httpbin.org/ip", proxies=proxy)

# print(res.text)

from selenium import webdriver
import time

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

print(driver.execute_script("return navigator.userAgent;"))

driver.get('https://www.httpbin.org/headers')


time.sleep(111)