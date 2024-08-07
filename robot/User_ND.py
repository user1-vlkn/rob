

from Print import Print
import sys
import asyncio
import nodriver as uc
import json
import random
import os
import requests



class User_ND:
    
    def __init__(self, url, move, experience, auth, movement, proxy, auth_data, conf, base_url, utm=False, cookie=False) -> None:
        self.url = url
        self.move = move
        self.experience = experience
        self.auth = auth
        self.movement = movement
        self.proxy = proxy
        self.error = 0
        self.conf = conf
        self.auth_data = auth_data
        self.top = None
        self.base_url = base_url
        self.utm = utm
        self.cookie = cookie
    
    
    async def launch_browser(self):
        try:
            self.browser = await uc.start()
        except Exception as e:
            Print.error(f"Failed to launch browser: {e}")
            raise
        return self.browser


    async def launch_proxy_browser(self, ipPort, username, password):
        try:
            self.browser = await uc.start(
                browser_args=[f"--proxy-server={ipPort}"]
            )

            self.username = username
            self.password = password

            self.main_tab = await self.browser.get("draft:,")
            self.main_tab.add_handler(uc.cdp.fetch.RequestPaused, self.req_paused)
            self.main_tab.add_handler(
                uc.cdp.fetch.AuthRequired, self.auth_challenge_handler
            )
            await self.main_tab.send(uc.cdp.fetch.enable(handle_auth_requests=True))
            return self.browser
        except Exception as e:
            Print.error(f"Failed to launch proxy browser: {e}")
            raise


    async def auth_challenge_handler(self, event: uc.cdp.fetch.AuthRequired):
        try:
            asyncio.create_task(
                self.main_tab.send(
                    uc.cdp.fetch.continue_with_auth(
                        request_id=event.request_id,
                        auth_challenge_response=uc.cdp.fetch.AuthChallengeResponse(
                            response="ProvideCredentials",
                            username=self.username,
                            password=self.password,
                        ),
                    )
                )
            )
        except Exception as e:
            Print.error(f"Error handling authentication challenge: {e}")


    async def req_paused(self, event: uc.cdp.fetch.RequestPaused):
        try:
            asyncio.create_task(
                self.main_tab.send(
                    uc.cdp.fetch.continue_request(request_id=event.request_id)
                )
            )
        except Exception as e:
            Print.error(f"Error while continuing paused request: {e}")
    
    
    async def getRandomString(self):
        
        try:
            with open('messages.json', 'r', encoding="utf-8") as j: 
                js =  json.load(j)
                
                return js[random.randint(0, len(js) - 1)]
                
        except Exception as e:
            Print.error(e)
    
    
    async def walk(self):
        
        try:
            pass
        
        except Exception as e:
            Print.error("[+] Error in method walk")
            Print.error(e)
    
    
    async def run(self):
        try:
            Print.log('[+] Start User')
            Print.log(self.proxy)
            self.driver = await self.launch_proxy_browser(f'{self.proxy['ip']}:{self.proxy['port']}', self.proxy['login'], self.proxy['pass'])
            
            url = self.url['url']
            url_start = self.conf['start_urls'][random.randint(0, len(self.conf['start_urls']) - 1)] if len(self.conf['start_urls']) > 1 else self.conf['start_urls'][0]
            
            _s_url = f"{url}{url_start}"
                
            _s_url = _s_url if 'http' in _s_url else f'https://{_s_url}'
            
            utm = random.randint(0, 1) if self.utm else False
                    
            Print.log(f'[+] Utm status: {utm}')
            if utm:
                        
                try:
                    Print.log('[+] Get UTM metric')
                    utm = requests.get(f'http://{self.base_url}/api/v1/getutmargs')
                            
                    Print.log(f'[+] UTM: {utm.text}')
                            
                    url = f'{url}{utm.text}'
                        
                except Exception as e:
                    Print.error('[+] Error in get UTM metric')
                    Print.error(e)
                    
            # ==============================
            #          Set Cookie
            # ==============================
            
            # self.page = await self.driver.get("https://httpbin.org/ip")
            # await self.page.sleep(3)
            
            # await self.page.close()
        
        except Exception as e:
            Print.error("[+] Error in method start User_ND")
            Print.error(e)
            await self.page.close()

        
            
    def start(self):
        
        try:
            
            uc.loop().run_until_complete(self.run())
            
        except Exception as e:
            Print.error(e)
    



if __name__ == "__main__":
    
    
    try:
        args = sys.argv
        
        Print.log(args)
        
        name_file = f'{args[1]}.json'
        
        with open(name_file, 'r') as f:
            data = json.loads(f.read())
            
            user = User_ND(
                data['url'],
                data['move'],
                data['experience'],
                data['auth'],
                data['movement'],
                data['proxy'],
                data['auth_data'],
                data['conf'],
                data['base_url'],
                data['utm'],
                data['cookie']                     
            )
            user.start()
        
        os.remove(name_file)
        
        
    
    except Exception as e:
        Print.error("[+] Error in main User_ND")
        Print.error(e)