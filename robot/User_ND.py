

from Print import Print
import sys
import asyncio
import nodriver as uc
import json
import random


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
            self.page = await self.driver.get("https://httpbin.org/ip")
            await self.page.sleep(3)
            
            await self.page.close()
            # self.driver = await self.launch_proxy_browser('207.244.217.165:6712', "cyipbegl", 'k0ffx4ses8m5')
        
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
        
        # Print.log(args[1])
        
        User_ND().start()
        
    
    except Exception as e:
        Print.error("[+] Error in main User_ND")
        Print.error(e)