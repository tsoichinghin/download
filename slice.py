from seleniumwire import webdriver
import random
import time

def slice():
    for _ in range(20):
        while True:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(r"user-data-dir=/home/tch/.config/google-chrome")
            chrome_options.add_argument(r'--profile-directory=Profile 1')

            proxy_options = {
                'proxy':{
                    'http':'http://user-lu4456881-region-hk:Qdi5pZ@as.rhyq9ffx.lunaproxy.net:12233'
                }
            }

            driver = webdriver.Chrome(seleniumwire_options = proxy_options, options = chrome_options)
            driver.set_page_load_timeout(60)

            try:
                driver.get("https://tab.sli.ce.it/")
                print("Page load succeed.")
                time_sleep = random.uniform(1, 5)
                time.sleep(time_sleep)
                break
            except:
                print("Page load timeout:")
                driver.quit()

slice()
