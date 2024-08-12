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
            
            Print.log(m)
            
            if len(m) == 0:
                Print.warning("[+] Not found links")
                return
            
            Print.log("[+] Get random link")
            link = m[random.randint(0, len(m) - 1)]
            
            Print.log(f'[+] Link {link}')
            
            a_href = await page.evaluate(f'''document.querySelectorAll("a[href='{link}']")''')
            Print.log(a_href)
            
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
                
                y = coords['top']
                    
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
            
            
            return 
            
            
            
            
            # links = page.locator('body').get_by_role('link').all()
            
            # if len(links) == 0:
            #     Print.error("[+] Not found links")
            #     return
            
            # m = []
                    
            # for i in links: m.append(i.get_attribute('href'))
            
            # Print.log("[+] Clear all hrefs")
            # m = Link.delete_d(m, close_urls)
            
            # if len(m) == 0:
            #     Print.warning("[+] Not found links")
            #     return
            
            # Print.log("[+] Get random link")
            # link = m[random.randint(0, len(m) - 1)]
            
            # link = page.locator(f"xpath=//a[@href='{link}']").all()
            
            # if len(link) == 0:
            #     Print.warning("[+] Not found links")
            #     return 
            
            # link_s = link[len(link) - 1]
            
            # Print.log('[+] Get coords link')
            # link = link_s.bounding_box()
            
            # Print.log(f"[+] Coords link {link}")
            
            # act.f_move_random_scroll()
            
            # viewport = pg.size()
            # view_h = viewport.height
            # view_w = viewport.width
            
            # padding_top = page.evaluate("document.documentElement.clientHeight")
            
            # ck = True
            # counter = 0
            # coords = link_s.bounding_box()
                
            # while ck:
                    
            #     if counter > 10:
            #         Print.warning('[+] Counter link scroll > 10')
            #         break
                    
            #     counter += 1
                    
            #     if coords['y'] > (view_h - 200):
            #         Print.log('[+] y > height view')
            #         act.d_scroll((coords['y'] - (view_h / 2)) * -1)
                    
            #     if coords['y'] < 100:
            #         Print.log('[+] y < height view')
            #         act.d_scroll(abs(coords['y']) + padding_top + (padding_top - view_h))
                    
            #     if coords['y'] > 100 and coords['y'] < (view_h - 200):
            #         Print.ok("[+] Scroll completed on element")
            #         ck == False
            #         break
                    
            #     Print.log('[+] Next step while scroll')
            #     coords = link_s.bounding_box()
            
            # Print.log(f"[+] Update coords")
            # link = link_s.bounding_box()
            
            # Print.log(f"[+] New coords {link}")
            
            # if link['x'] > 0 and link['y'] > 0:
                
            #     if link['x'] < view_w and link['y'] < view_h:
                    
            #         Print.warning(f"[+] Click {link}")
            #         act.d_click(link)
            
            
            # Print.ok('[+] Link is done.')
            
        except Exception as e:
            Print.error("[+] Error in Link class")
            Print.error(e)