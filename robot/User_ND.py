

import sys
import asyncio
import nodriver as uc
import json
import random
import os
import requests
from Actions import Actions
import time
from Cookie import Cookis
from Print import Print
from Study import Study
from Auth import Auth
from Scroll import Scroll
from Move import Move
from Link import Link
from Some_DO import Some_DO
from Sleep import Sleep
from GetSizePanel import GetSizePanel



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
            self.browser = await uc.start(
                 browser_args=[
                    '--load-extension=C:\\Users\\User\\Desktop\\rob\\robot\\0.3.2_0',
                    '--start-maximized'
                    ]
            )
        except Exception as e:
            Print.error(f"[+] Failed to launch browser: {e}")
            raise
        return self.browser


    async def launch_proxy_browser(self, ipPort, username, password):
        try:
            self.browser = await uc.start(
                browser_args=[
                    f"--proxy-server={ipPort}",
                    '--load-extension=C:\\Users\\User\\Desktop\\rob\\robot\\0.3.2_0',
                    '--start-maximized'
                    ]
            )

            self.username = username
            self.password = password

            self.main_tab = await self.browser.get("draft:,")
            
            self.main_tab.add_handler(uc.cdp.fetch.RequestPaused, self.req_paused)
            
            self.main_tab.add_handler(uc.cdp.fetch.AuthRequired, self.auth_challenge_handler)
            
            await self.main_tab.send(uc.cdp.fetch.enable(handle_auth_requests=True))
            
            return self.browser
        
        except Exception as e:
            Print.error(f"[+] Failed to launch proxy browser: {e}")
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
            Print.error(f"[+] Error handling authentication challenge: {e}")


    async def req_paused(self, event: uc.cdp.fetch.RequestPaused):
        try:
            asyncio.create_task(
                self.main_tab.send(
                    uc.cdp.fetch.continue_request(request_id=event.request_id)
                )
            )
        except Exception as e:
            Print.error(f"[+] Error while continuing paused request: {e}")
    
    
    async def getRandomString(self):
        
        try:
            with open('messages.json', 'r', encoding="utf-8") as j: 
                js =  json.load(j)
                
                return js[random.randint(0, len(js) - 1)]
                
        except Exception as e:
            Print.error(e)
    
    
    async def walk(self) -> bool:
        
        try:
            
            Print.ok('[+] Next step')
            
            exp = self.movement['experience']
            
            range_walk = random.randint(int(exp['min']),  (exp['max']))
            
            Print.log(f'[+] Range walk {range_walk}')
            
            await Link.link(self.page, self.actions, self.conf['close_urls'])
            
            return True
            
            for _ in range(0, range_walk):
                
                Print.log("[+] Some do step")
                Some_DO.some_do(self.page, self.actions, self.conf['some_do']['check_el'])
                
                event = ["read_text", "watch_img", "auth", "scroll", "move"]
        
                Print.log('[+] Get random behavior')
                event_el = event[random.randint(0, len(event) - 1)]
                
                Print.warning(f'[+] Type event [{event_el}]')
                
                if event_el == 'read_text': Study.study("txt", self.page, self.actions, self.top)
                
                if event_el == 'watch_img': Study.study("img", self.page, self.actions, self.top)
                
                if event_el == 'auth' and self.auth:
                    pass
                    # Auth.auth(self.page, self.actions, self.auth_data)
                
                if event_el == 'scroll': await Scroll.scroll(self.page, self.actions)
                
                if event_el == 'move': await Move.move(self.actions)
                
            Print.log('[+] Find link for click')
            # Link.link(self.page, self.actions, self.conf['close_urls'])
            
            Sleep.zZz(1000)
            Print.log('\n')

            return True
        
        except Exception as e:
            Print.error(e)
            return False
    
     
    async def run(self):
        
        try:
            
            Print.log('[+] Start User')
            
            # self.driver = await self.launch_proxy_browser(f'{self.proxy['ip']}:{self.proxy['port']}', self.proxy['login'], self.proxy['pass'])
            
            self.driver = await self.launch_browser()
            self.page = self.driver
            
            
            url = self.url['url']
            url_start = self.conf['start_urls'][random.randint(0, len(self.conf['start_urls']) - 1)] if len(self.conf['start_urls']) > 1 else self.conf['start_urls'][0]
            
            move = self.movement['move']
                    
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
            
            
            
            
            self.page = await self.driver.get("https://royal-vulkan.ru/")
          
            self.actions = Actions(move['mousemove'], move['scroll'], self.top)
            
            self.actions.d_wait_random({"min": 4, "max": 5})
                
            time_s = self.url['time']
                
            time_s = random.randint(int(time_s[0]), int(time_s[1]))
                
            Print.log(f"[+] Time walk {time_s}")
                
            time_s = int(time.time()) + time_s
                
            Print.log(f'[+] Full time in sec {time_s}')
                
            while time_s > int(time.time()):
                    
                if self.error > 5:
                    Print.error('[+] Error limit exceeded')
                    return False
                    
                res = await self.walk()
                    
                if res: Print.ok('[+] Walk without mistakes')
                    
                else:
                    Print.error("[+] Walk with mistakes")
                    self.error += 1
                    
                res = None
                
                Print.ok("[+] Time walk is done.")
                
                await self.page.close()
                return True
        
        except Exception as e:
            Print.error("[+] Error in method start User_ND")
            Print.error(e)
            await self.page.close()

        
            
    def start(self):
        
        try:
            self.top = GetSizePanel().getTop("chrome")
            
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