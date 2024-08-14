

import random
import json
import requests
from Print import Print



class Proxy:
    
    @staticmethod
    def file():
        try:
            file = json.loads(open('proxy.json', 'r', encoding='utf-8').read())

            t = file['proxy']
            
            return {'proxy': t[random.randint(0, len(t) - 1)]} if len(t) != 0 else False
                
        except Exception as e:
            Print.error(e)
            return False
    
    
    @staticmethod
    def url():
        try:

            auth = {'login': 'mix266000QSUI', 'pass': 'j3abNOMS'}
            url = f'https://fineproxy.org/api/getproxy/?r=1&format=txt&type=http_auth&login={auth['login']}&password={auth['pass']}'

            res = requests.get(url=url)

            st = res.text.split(":")

            res_json = {
                'ip': st[0],
                'port': st[1],
                'login': auth['login'],
                'pass': auth['pass']
            }

            return {'proxy': res_json}
            
        except Exception as e:
            Print.error(e)
            return False
    
    @staticmethod
    def n_pro():
        res_json = {
            'ip': 'portal.anyip.io',
            'port': '1080',
            'login': 'user_6ca446',
            'pass': 'dfb877'
        }
        
        return {'proxy': res_json}
        
    
    @staticmethod
    def pr_url(ip):

        m = ['3081', '3082', '3083', '3084', '3085', '3086', '3087', '3088','3089','3090','3091','3092', '3093']

        res_json = {
            'ip': ip,
            'port': m[random.randint(0 , len(m) - 1 )],
            'login': 'PPR02BYGXV2',
            'pass': 'ZgM0Y4DxRR7GUr'
        }
        
        return {'proxy': res_json}
    
    
    @staticmethod
    def test_proxy():
        
        try: 
            with open('./static/proxy.txt') as f:
                
                myList = [ line.split() for line in f ]
                flatList = [ item for sublist in myList for item in sublist ]
                
                flatList = flatList[random.randint(0, len(flatList) - 1)]
                ip_s = flatList.split("@")
                ip_s_l = ip_s[0].split(":")
                ip = ip_s_l[0]
                port = ip_s_l[1]
                login_s = ip_s[1].split(":")
                login = login_s[0]
                pass_s = login_s[1]
                
                res_json = {
                    'ip': ip,
                    'port': port,
                    'login': login,
                    'pass': pass_s
                }
                
                return {'proxy': res_json}
            
        except Exception as e:
            Print.error("[+] Error in test proxy method")
            Print.error(e)
            return {'proxy': {}}
    
    
    @staticmethod
    def fuck_nigga():
        res_json = {
                    'ip': "157.52.253.244",
                    'port': "6204",
                    'login': "cyipbegl",
                    'pass': "k0ffx4ses8m5"
                }
                
        return {'proxy': res_json}
    
    
    @staticmethod
    def getproxy():
        
        # m = [Proxy.test_proxy(), Proxy.pr_url('185.46.84.234'),  Proxy.pr_url('146.185.207.3'),Proxy.n_pro()]
        m = [ Proxy.pr_url('146.185.207.3') ]
        return m[random.randint(0, len(m) - 1)]
        # return Proxy.test_proxy()


