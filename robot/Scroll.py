
import pyautogui as pg
import random
from Print import Print


class Scroll:
    
    
    @staticmethod
    def scroll(page, act):
        
        try:
        
            Print.log("[+] Scroll")
        
            scroll_max = page.evaluate("Math.max(document.body.scrollHeight, document.documentElement.scrollHeight,document.body.offsetHeight, document.documentElement.offsetHeight, document.body.clientHeight, document.documentElement.clientHeight)")
        
            viewport = pg.size().height
        
            if viewport < scroll_max:
            
                Print.log('[+] Еthere is a possibility to scroll')
            
                count = random.randint(5, 10)
            
                Print.log(f'[+] Count scrolls: {count} ')
            
                for i in range(0, count):
                
                    act.f_move_random_scroll()

                    pos_scroll_now = page.evaluate("window.pageYOffset")

                    if pos_scroll_now < (scroll_max / 2):
                        act.d_scroll((random.randint(0, scroll_max - pos_scroll_now) - 1) * - 1)

                    if pos_scroll_now > (scroll_max / 2):
                        act.d_scroll(random.randint(0, pos_scroll_now))
                    
                    act.d_wait_random({"min": 1, "max": 3})
        
        except Exception as e:
            Print.error('[+] Error in Scroll class')
            Print.error(e)
        
        
        Print.ok("Scrolling is done.")