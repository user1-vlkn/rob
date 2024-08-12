import pyautogui as pg
import random
from Print import Print
from Executor import Executor
import time


class Link:
    
    
    @staticmethod
    async def delete_d(m, close_urls):
        m = list(dict.fromkeys(m))
        for i in close_urls:
            if i in m: m.remove(i)
        return m
    
    
    @staticmethod
    async def link(page, act, close_urls):
        
        try:
            
            Print.log("[+] Link")
            
            Print.log("[+] Get all hrefs")
            
            act.d_wait_random({"min": 1, "max": 2})
            
            links = await Executor.locator_href(page, "a")
            
            m = await Link.delete_d(links, close_urls)
            
            if len(m) == 0:
                Print.warning("[+] Not found links")
                return
            
            Print.log("[+] Get random link")
            link = m[random.randint(0, len(m) - 1)]
            
            Print.log(f'[+] Link {link}')
            
            a_href = await page.evaluate(f'''document.querySelectorAll("a[href='{link.replace("'", "\'")}']")''')
            
            if a_href == None:
                Print.warning("[+] Not found elem")
                return
            
            if len(a_href) == 0:
                Print.warning("[+] Not found elem")
                return
            
            el_pos = random.randint(0, len(a_href) - 1)
            
            link = f'''a[href='{link}']'''
            
            coords = await Executor.coords(page, link, el_pos )
            
            Print.log(f"[+] Coords link {coords}")
            
            act.f_move_random_scroll()
            
            viewport = pg.size()
            view_h = viewport.height
            view_w = viewport.width
            
            padding_top = page.evaluate("document.documentElement.clientHeight")
            
            ck = True
            counter = 0
            
            coords = await Executor.coords(page, link, el_pos )
            
            while ck:
                    
                if counter > 10:
                    Print.warning('[+] Counter link scroll > 10')
                    break
                    
                counter += 1
                
                y = int(coords['top'])
                    
                if y > (view_h - 200):
                    Print.log('[+] y > height view')
                    act.d_scroll((y - (view_h / 2)) * -1)
                    
                if y < 100:
                    Print.log('[+] y < height view')
                    act.d_scroll(abs(y) + padding_top + (padding_top - view_h))
                    
                if y > 100 and y < (view_h - 200):
                    Print.ok("[+] Scroll completed on element")
                    ck == False
                    break
                    
                Print.log('[+] Next step while scroll')
                coords = await Executor.coords(page, link, el_pos )
            
            Print.log(f"[+] Update coords")
            coords = await Executor.coords(page, link, el_pos )
            
            Print.log(f"[+] New coords {coords}")
            
            if coords['left'] > 0 and coords['top'] > 0:
                
                if coords['left'] < view_w and coords['top'] < view_h:
                    
                    Print.warning(f"[+] Click {coords}")
                    act.d_click(coords)
            
            
            Print.ok('[+] Link is done.')
            
            
        except Exception as e:
            Print.error("[+] Error in Link class")
            Print.error(e)