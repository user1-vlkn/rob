


import sys
sys.path.insert(1, '../')
import pyautogui as pg
import time
import os
import random
import numpy as np
from Print import Print
from Actions import Actions
from playwright.sync_api import sync_playwright, Playwright



class Study:
        
    @staticmethod
    def reads_carefully(obj, act):
        
        Print.log("[+] Read carefully")
        
        obj_w = int(obj['width'])
        obj_h = int(obj['height'])
        
        mass = []
        
        for i in range(0, int(obj_h / 10)):
            
            h = i * 10
            
            for i1 in range(0, int(obj_w / 10)):
                
                w = i1 * 10
                
                mass.append({
                    'x': random.randint(w, w + 10) + obj_w,
                    'y': random.randint(h, h + 10) + obj_h
                })
        
        for i2 in mass: act.mosemove(i2['x'], i2['y'])
    
    
    
    @staticmethod
    def just_drives(obj, act):
        
        Print.log("[+] Just driver")
        
        mass = []
        
        for i in range(0, random.randint(5, 15)):
            
            mass.append({ 
                "x": random.randint(0, int(obj['width']) ) + int(obj['x']),
                "y": random.randint(0, int(obj['height']) ) + int(obj['y'])
            })
            
        for i in mass: act.mosemove(i['x'], i['y'])
    
    
    @staticmethod
    def study(t, page, act, top):
        
        try:
            
            Print.log("[+] Start study")
            
            t = 'p' if t == 'txt' else 'img'
            
            act.d_wait_random({"min": 1, "max": 2})
            
            el = page.locator(f"xpath=//{t}").all()
            
            if len(el) == 0: 
                Print.warning(f"[+] Element {t} is not found")
                return
        
            Print.log(f"[+] Length elem : {len(el)}")
            
            el = el[random.randint(0, len(el) - 1)]
            
            Print.log(f'[+] Element {el}')
            
            if el == None:
                Print.error("[+] Element is None")
                return
            
            coords = el.bounding_box()
            
            if el == None:
                Print.error("[+] Coords is None")
                return
            
            
            if coords == None:
                Print.error("[+] Coords in None")
                return
            
            Print.log(f"[+] Coords {coords}")
            
            view_h = pg.size().height
            
            padding_top = page.evaluate("document.documentElement.clientHeight")
            
            act.f_move_random_scroll()
            
            
            if coords['y'] > (view_h - 100) or coords['y'] < 0:
                
                ck = True
                counter = 0
                coords = el.bounding_box()
                
                while ck:
                    
                    if counter > 10:
                        Print.warning('[+] Counter study scroll > 10')
                        break
                    
                    counter += 1
                    
                    if coords['y'] > (view_h - 200):
                        Print.log('[+] y > height view')
                        act.d_scroll((coords['y'] - (view_h / 2)) * -1)
                    
                    if coords['y'] < 100:
                        Print.log('[+] y < height view')
                        act.d_scroll(abs(coords['y']) + padding_top + (padding_top - view_h))
                    
                    if coords['y'] > 100 and coords['y'] < (view_h - 200):
                        Print.ok("[+] Scroll completed on element")
                        ck == False
                        break
                    
                    Print.log('[+] Next step while scroll')
                    coords = el.bounding_box()
                    
            
            Print.log("[+] Update coords")
            
            coords = el.bounding_box()
            
            coords['y'] = coords['y'] + int(top)
            
            Print.log(f"[+] Coords {coords}")
            
            if t == 'txt':
                
                Print.log('[+] Study TXT')
                
                Study.reads_carefully(coords, act) if random.randint(0, 1) else Study.just_drives(coords, act)
                
            else:
                
                Print.log('[+] Study IMG')
                
                Study.just_drives(coords, act)
            
            Print.ok("[+] Study is done.")
        
        except Exception as e:
            Print.error(e)
