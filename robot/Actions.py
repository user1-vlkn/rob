
import sys
sys.path.insert(1, '../')
import time
import os
import random
import numpy as np
from Print import Print
from playwright.sync_api import sync_playwright, Playwright

class Actions:
    
    def __init__(self, mouse=None, scroll=None, page=None) -> None:
        self.mouse = mouse
        self.scroll = scroll
        self.page = page
    
    
    def page_size(self):
        
        page_size = self.page.evaluate(""" _=> [document.documentElement.clientWidth, document.documentElement.clientHeight] """)
            
        if page_size != None:
                
            return page_size if len(page_size) != 0 else []
                    
        else: Print.warning("[+] Can not get size window") 
        
    
    
    def t(self, a: int, b: int): return random.randint(a, b)
    
    
    def d_wait_random(self, d: dict): time.sleep(self.t(int(d['min']), int(d['max'])))
    
    
    def mosemove(self, x, y, p_x = 0, p_y = 0):
        
        page_size = self.page_size()
        
        if len(page_size):
            if p_x == 0 and p_y == 0:
                p_x = self.t(0, page_size[0])
                p_y = self.t(0, page_size[1])
            
            G_0 = self.t(self.mouse['G_0'] - 10, self.mouse['G_0'] + 10)
            W_0 = self.t(self.mouse['W_0'] - 10, self.mouse['W_0'] + 10)
            M_0 = self.t(self.mouse['M_0'] - 10, self.mouse['M_0'] + 10)
            D_0 = self.t(self.mouse['D_0'] - 10, self.mouse['D_0'] + 10)
            
            return self.wind_mouse(p_x, p_y, x, y, G_0, W_0, M_0, D_0)
        
        return 0, 0

        
    def wind_mouse(self, start_x, start_y, dest_x, dest_y, G_0, W_0, M_0, D_0):
        
        sqrt3 = np.sqrt(2)
        sqrt5 = np.sqrt(10)

        current_x, current_y = start_x, start_y
        v_x = v_y = W_x = W_y = 0
        
        
        while (dist := np.hypot(dest_x - start_x, dest_y - start_y)) >= 1:
            W_mag = min(W_0, dist)
            if dist >= D_0:
                
                W_x = W_x / sqrt3 + (2 * np.random.random() - 1) * W_mag / sqrt5
                W_y = W_y / sqrt3 + (2 * np.random.random() - 1) * W_mag / sqrt5
                
            else:
                
                W_x /= sqrt3
                W_y /= sqrt3
                
                if M_0 < 3: M_0 = np.random.random() * 3 + 3
                else: M_0 /= sqrt5
                    
                    
            v_x += W_x + G_0 * (dest_x - start_x) / dist
            v_y += W_y + G_0 * (dest_y - start_y) / dist
            
            v_mag = np.hypot(v_x, v_y)
            
            if v_mag > M_0:
                
                v_clip = M_0 / 2 + np.random.random() * M_0 / 2
                v_x = (v_x / v_mag) * v_clip
                v_y = (v_y / v_mag) * v_clip
                
            start_x += v_x
            start_y += v_y
            
            move_x = int(np.round(start_x))
            move_y = int(np.round(start_y))
            
            if current_x != move_x or current_y != move_y:
                time.sleep(self.t(1000, 1400) / 10000)
                self.page.mouse.move(abs(move_x), abs(move_y))
                current_x = move_x
                current_y = move_y
        
        return current_x, current_y
    
    
    def f_move_random_scroll(self):
        
        try:
            
            page_size = self.page_size()
            
            if len(page_size):
                view_h = page_size[0]
                view_w = page_size[1]
                
                pro_20 = lambda a : int((a / 100) * 20)
            
                x = self.t(pro_20(view_w), view_w - pro_20(view_w))
                y = self.t(pro_20(view_h), view_h - pro_20(view_h))
            
                # ========================
                self.mosemove(x, y)
                # ========================
            
                time.sleep(self.t(200, 600) / 1000)
            
        except Exception as e:
            Print.error('[+] Error in move_random_scroll')
            Print.error(e)

