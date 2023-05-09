import time
import json

from selenium import webdriver

def load_cookie():
    f = open('cookie.txt', 'r')
    str = f.read().replace('False', 'false').replace('True', 'true')
    print(str)
    return json.loads(str)

def time_update(targetTime):
    while True:
        now = time.time()
        timeToWait = targetTime - now
        print(timeToWait)
        if timeToWait < 1.2:
            driver.get(url)
            # viewer1 = driver.find_element_by_xpath('//*[@id="dmViewerBlock_DmViewerBlock"]/div[2]/div/div[1]/div[3]/i')
            while True:
                try:
                    driver.find_element_by_xpath('//*[@id="dmViewerBlock_DmViewerBlock"]/div[2]/div/div[1]/div[3]/i').click()
                    break
                except Exception as e:
                    print(e)
                    continue
            while True:
                try:
                    driver.find_element_by_xpath('//*[@id="dmViewerBlock_DmViewerBlock"]/div[2]/div/div[2]/div[3]/i').click()
                    break
                except Exception as e:
                    print(e)
                    continue
            while True:
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="dmOrderSubmitBlock_DmOrderSubmitBlock"]/div[2]/div/div[2]/div[3]/div[2]').click()
                finally:
                    continue
        else:
            time.sleep(timeToWait/2)

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
chrome_driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.maximize_window()
driver.implicitly_wait(10)
item_url = "https://m.damai.cn/damai/detail/item.html?itemId=716759481923"
url = 'https://m.damai.cn/app/dmfe/h5-ultron-buy/index.html?buyParam=716759481923_2_5007288349052&buyNow=true&exParams=%257B%2522channel%2522%253A%2522damai_app%2522%252C%2522damai%2522%253A%25221%2522%252C%2522umpChannel%2522%253A%2522100031004%2522%252C%2522subChannel%2522%253A%2522damai%2540damaih5_h5%2522%252C%2522atomSplit%2522%253A1%257D&spm=a2o71.project.0.bottom&sqm=dianying.h5.unknown.value#showViewer'


script = '''
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
})
'''

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})

driver.get(item_url)
cookies = load_cookie()
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get(item_url)

time_update(1683601200)

# driver.get(url)


