from Print import Print
import pyautogui as pg
import random

class Move:
    
    
    @staticmethod
    def move(act, page):
        
        try:
            
            Print.log("[+] Move rundom")
            count = random.randint(5, 15)
            
            Print.log(f'[+] Count move {count}')
            
            page_size = page.evaluate(""" _=> [document.documentElement.clientWidth, document.documentElement.clientHeight] """)
            
            Print.log(f'[+] Page size {page_size}')
            
            if page_size != None:
                
                if len(page_size) != 0:
                    
                    x_s = 0
                    y_s = 0
                    
                    for i in range(1, count):
                        x = random.randint(0, page_size[0])
                        y = random.randint(0, page_size[1])
                        
                        Print.log("[+] Move")
                        
                        x_s, y_s = act.mosemove(x, y, x_s, y_s)
                        
                        Print.warning(f'x: {x_s} y: {y_s}')
                        
                    
            else: Print.warning("[+] Can not get size window") 
            
            Print.ok("[+] Move rundom is done.")
        
        except Exception as e:
            Print.error("[+] Error in random_move class")
            Print.error(e)
        
