

from Print import Print



class Some_DO:
    
    @staticmethod
    def some_do(page, act, s):
        
        for i in  s:
            
            try:
                
                Print.log("[+] Start some do")
                a = page.locator(i['el']).all()
                
                if len(a) == 0:
                    Print.warning(f"[+] Not found elem {i['el']}")
                    return
                    
                if isinstance(a, list):
                        
                    Print.log("[+] Some elem is list")
                        
                    if len(a) > 0:
                        Print.log('[+] Some do elem is > 0')
                            
                        link = page.evaluate(f"document.querySelector(\"{i['el1']}\").getBoundingClientRect()")
                        
                        Print.log(f'[+] Link {link}')
                            
                        if link != None: act.d_click(link)
                        
                
            except Exception as e:
                Print.error('[+] Error in Some DO')
                Print.error(e)