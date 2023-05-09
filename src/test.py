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
        if timeToWait < 0.6:
            driver.get(url)
            viewers = driver.find_element_by_class_name('viewer').find_elements_by_class_name('iconfont')
            viewers[0].click()
            while True:
                driver.find_element_by_xpath(
                    '//*[@id="dmOrderSubmitBlock_DmOrderSubmitBlock"]/div[2]/div/div[2]/div[3]/div[2]').click()
        else:
            time.sleep(timeToWait/2)

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
chrome_driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.maximize_window()
driver.implicitly_wait(10)
item_url = "https://m.damai.cn/damai/detail/item.html?itemId=713729510767"
url = 'https://m.damai.cn/app/dmfe/h5-ultron-buy/index.html?buyParam=713729510767_1_4997520153992&buyNow=true&exParams=%257B%2522channel%2522%253A%2522damai_app%2522%252C%2522damai%2522%253A%25221%2522%252C%2522umpChannel%2522%253A%2522100031004%2522%252C%2522subChannel%2522%253A%2522damai%2540damaih5_h5%2522%252C%2522atomSplit%2522%253A1%257D&spm=a2o71.project.0.bottom&sqm=dianying.h5.unknown.value#showViewer'


script = '''
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
})
'''

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})

driver.get(url)
time.sleep(80)

cookie = driver.get_cookies()
print(str(cookie))
f = open('cookie.txt', 'w+')
f.write(str(cookie).replace('\'', '\"'))
f.close()