
import sys
sys.path.insert(1, '../')

import time
from Print import Print
import requests
import json
import random
from User import User
from Sleep import Sleep




class Robot:
    
    def __init__(self, id, base_url, url=None) -> None:
        self.id = id
        self.base_url = base_url
        self.url = url
    
    
    def request_m(self, url):
        try:
            
            res = requests.get(f'http://{self.base_url}{url}')
            
            return json.loads(res.text) if res.status_code == 200 else False
        
        except Exception as e:
            Print.error("[+] Error in method request")
            Print.error(e)
            return False
    
    def start(self):
        
        try:
            
            while True:
                
                try:
                    
                    Print.log("[+] Get proxy")
                    proxy = self.request_m("/api/v1/getproxy")
                    
                    if proxy == False: Print.error("[+] Error in get proxy")
                    
                    Print.log(f'[+] Proxy status {proxy['status']}')
                    
                    if proxy and proxy['status']:
                        
                        Print.ok("[+] The request to receive the proxy is successful")
                        
                        behavior = self.request_m(f"/api/v1/behavior/{self.id}")
                        
                        if behavior and behavior['status']:
                            
                            Print.ok("[+] The request to receive the behavior is successful")
                            
                            if behavior['data']['in_work']:
                                
                                Print.log(f"[+] Robot id: {self.id} start walk")
                                
                                data = behavior['data']
                                
                                Print.log("[+] Start visits")
                                
                                for i in data['visits']:
                                    
                                    Print.log(f'[+] Visits url {i['url']}')
                                    
                                    Print.log("[+] Request getconfvisitorurl in visits")
                                    
                                    # conf = self.request_m(f"/api/v1/getconfvisitorurl/{i['url']}")
                                    
                                    Print.log("test")
                                    conf = self.request_m(f"/api/v1/getconfvisitorurl/dns-shop.ru")
                                    
                                    Print.log(conf)
                                    
                                    
                                    if conf['status']:
                                        
                                        Print.warning('[+] Status getconfvisitorurl is [ true ]')
                                        
                                        user = User(
                                            i, 
                                            data['move'],
                                            data['experience'],
                                            False,
                                            data['movement'],
                                            proxy['data']['proxy'],
                                            data['auth_data'],
                                            conf['data'],
                                            self.base_url,
                                            utm=data['utm'],
                                            cookie=False
                                            )
                                        
                                        user.run()
                                        
                                    else:
                                        Print.warning('[+] Status getconfvisitorurl was [ false ]')
                                
                                # main User
                                # ============================================================================
                                
                                Print.log("[+] Request getconfvisitorurl for main user")
                                conf = self.request_m(f"/api/v1/getconfvisitorurl/{data['url']['url']}")
                                
                                if conf['status']:
                                    
                                    user = User(
                                        data['url'],
                                        data['move'],
                                        data['experience'],
                                        data['auth'],
                                        data['movement'],
                                        proxy['data']['proxy'],
                                        data['auth_data'],
                                        conf['data'],
                                        self.base_url,
                                        utm=data['utm'],
                                        cookie=data['cookie'],
                                        
                                        )
                                    
                                    user.run()
                                
                            else:
                                
                                sl = behavior['data']['sleep']
                                
                                Print.log(f"[+] 'in_work' is false ")
                                
                                Sleep.zZz(sl)
                                        
                                Print.log('\n')
                        
                        else: Print.error("[+] The request to receive the behavior is not successful")
                    
                    else: Print.error("[+] The request to receive the proxy is not successful")   
                        
                except Exception as e: Print.error(e)
                
                time.sleep(1)
                break
            
        except Exception as e:
            Print.error("[+] Error in start method")
            Print.error(e)
        
        

if __name__ == '__main__':
    
    try:
        
        args = sys.argv
        
        if len(args) >= 2:
            
            Print.ok("[+] Start app ROBOT")
            
            Robot(args[1], args[2], None if len(args) <= 3 else args[3]).start()
        
        else:
            Print.error("[+] The program is running without arguments ")
    
    except Exception as e:
        Print.error("[+] Error in main")
        Print.error(e)
    
    