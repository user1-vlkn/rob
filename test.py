from nodriver import start, cdp, loop
import asyncio
import time 
    
async def ev_nodriver():
    browser = await start(headless=False)
    page = await browser.get('https://learn.javascript.ru/coordinates')
    await page.set_window_state(0,0, 500, 500, "normal")
    await page.send(cdp.input_.dispatch_mouse_event("mouseMoved", x=100, y=200))
    await page.send(cdp.input_.dispatch_mouse_event("mouseReleased", x=100, y=500))
    s = await page.evaluate("""let s = [];for (i of [...document.querySelectorAll('a')]) {let  rect = i.getBoundingClientRect();s.push({top: rect.top,right: rect.right,bottom: rect.bottom,left: rect.left,width: rect.width,height: rect.height,x: rect.x,y: rect.y})
                                    };s""")
    print(s)
    await page.save_screenshot()
      

if __name__ == "__main__":
    asyncio.run(ev_nodriver())