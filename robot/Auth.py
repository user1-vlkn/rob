from Print import Print

class Auth:
    
    
    @staticmethod
    def auth(page, act, auth_data):
        
        try:
            Print.log("[+] Auth")
            
            logged_user = page.locator("xpath=//a[@href='/popup-messagebox']").all()
            
            if len(logged_user) != 0:
                Print.warning("[+] User is logged")
                return
        
            Print.log("[+] User is not logged")
            
            act.d_wait_random({"min": 1, "max": 2})
            
            popup_login = page.locator("xpath=//a[@href='/popup-login']").all()
            
            if len(popup_login) == 0:
                Print.error("[+] Eleme /popup-login not found")
                return
            
            Print.log("[+] Click /popup-login")
            act.d_click(popup_login[0].bounding_box())
            
            Print.log("[+] Random wait")
            act.d_wait_random({"min": 1, "max": 2})
            
            type_login = page.locator(f"xpath=//div[@data-popup-tabs-name='{auth_data['type']}']").all()
            
            if len(type_login) == 0:
                Print.error("[+] Eleme {type_login} not found")
                return
            
            Print.log(f"[+] Click data-popup-tabs-name={auth_data['type']}")
            act.d_click(type_login[0].bounding_box())
            
            sign_in = page.locator(f"xpath=//input[@id='sign-in-{auth_data['type']}']").all()
            
            if len(sign_in) == 0:
                Print.error("[+] Eleme {type_login} not found")
                return
            
            act.d_click(sign_in[0].bounding_box())
            
            act.d_wait_random({"min": 1, "max": 2})
            
            act.write_text(auth_data['login'])
            
            act.d_wait_random({"min": 1, "max": 2})
            
            pass_s = 'sign-in-password' if auth_data['type'] == 'email' else f'sign-in-{auth_data['type']}-password'
            
            pass_input = page.locator(f"xpath=//input[@id='{pass_s}']").all()
            
            if len(pass_input) == 0:
                Print.error(f"[+] Eleme {pass_s} not found")
                return
            
            act.d_click(pass_input[0].bounding_box())
            
            act.d_wait_random({"min": 1, "max": 2})
            
            act.write_text(auth_data['pass'])
            
            act.d_wait_random({"min": 1, "max": 2})
            
            submit = page.locator(f"xpath=//button[@data-test='submit_button']").all()
            
            if len(submit) == 0:
                Print.error("[+] Eleme {submit_button} not found")
                return
            
            act.d_click(submit[0].bounding_box())
            
            act.d_wait_random({"min": 2, "max": 3})
            
            
            
            
        except Exception as e:
            Print.error("[+] Error in AUTH")
            Print.error(e)


