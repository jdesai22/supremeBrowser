from selenium import webdriver
from config import keys
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# assuming we ran: harvester recaptcha-v2 -d guerrillamail.com -k 6LcIHdESAAAAALVQtprzwjt2Rq722tkxk-RDQ0aN
# token = fetch.token('supremenewyork.com')
# print('Token:', token)

import logging
from threading import Thread
import threading

import harvester
from harvester import Harvester
from harvester import fetch

# @timeme
def checkStock(kw, negkw):
    url = "https://www.supremenewyork.com/mobile_stock.json"
    # r = requests.get(url)
    response = requests.get(url, headers={'User-Agent': 'Mozilla'})
    response.encoding = 'utf-8'
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    category = "shirts"


    for i in range(0, len(kw)):
        kw[i] = kw[i].lower()

    items = []
    for i in jsonResponse["products_and_categories"]["new"]:
        items.append(i["name"])

    # words = []

    highestCount = 0
    k = 0
    item =""
    for i in items:
        relevanceCount = 0
        words = i.split()
        for s in words:
            if s.lower() in kw:
                relevanceCount += 1
            elif s.lower() in negkw:
                relevanceCount -= 1

        if relevanceCount > highestCount:
            highestCount = relevanceCount
            item = i
        k+=1

    category = ""
    for i in jsonResponse["products_and_categories"]["new"]:
        if i["name"] == item:
            category = i["category_name"]
            break

    return [item, category]

def getKeywords(strKW):
    return [i.strip() for i in strKW.split(',')]



def order(src):
    # s = "//assets.supremenewyork.com/193760/vi/B7xrL9A8ACU.jpg"
    driver.find_element_by_xpath("//a[contains(text(), '{}')]".format(src)).click()

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'commit')))
    except:
        print("out of stock")
        exit(1)
    # add to cart
    driver.find_element_by_name('commit').click()
    # element.click()

    # wait for checkout button element to load
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'checkout')))
    checkout_element = driver.find_element_by_class_name('checkout')
    checkout_element.click()

    # fill out checkout screen fields
    driver.find_element_by_id('order_billing_name').send_keys(keys['name'])
    driver.find_element_by_id('order_email').send_keys(keys['email'])
    driver.find_element_by_id('order_tel').send_keys(keys['phone_number'])
    driver.find_element_by_id('bo').send_keys(keys['street_address'])
    driver.find_element_by_id('order_billing_zip').send_keys(keys['zip_code'])
    # driver.find_element_by_id('order_billing_city').send_keys(keys['city'])

    driver.find_element_by_id('rnsnckrn').send_keys(keys['card_number'])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(keys["month_exp"])).click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(keys["year_exp"]-2019)).click()
    driver.find_element_by_id('orcer').send_keys(keys['card_cvv'])

    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
    checkoutDelay = .5
    time.sleep(checkoutDelay)
    # pay = str(input("ready to go"))


    # assuming we ran: harvester recaptcha-v2 -d guerrillamail.com -k 6LcIHdESAAAAALVQtprzwjt2Rq722tkxk-RDQ0aN

    process_payment = driver.find_element_by_xpath('//*[@id="pay"]/input')
    process_payment.click()


def createHarvest():
    #  sitekey = 6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz
    harvester = Harvester()
    tokens = harvester.intercept_recaptcha_v2(
        domain='www.supremenewyork.com',
        sitekey='6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz'
    )
    server_thread = Thread(target=harvester.serve, daemon=True)
    server_thread.start()

    # launch a browser instance where we can solve the captchas
    harvester.launch_browser()

    try:
        while True:
            # block until we get sent a captcha token and repeat
            token = tokens.get()
            print('we just recived a token:', token)
    except KeyboardInterrupt:
        pass

def task():
    kw = input("Enter Keywords: ")
    negkw = input("Enter Negative Keywords: ")
    kw = getKeywords(kw)
    negkw = getKeywords(negkw)
    webInfo = checkStock(kw, negkw)
    item = webInfo[0]
    category = webInfo[1]


    driver.get("https://www.supremenewyork.com/shop/all/" + category)
    # order()
    init = time.time()
    order(item)
    final = time.time()
    el = final - init
    print(el)

    element = driver.find_element_by_id("g-recaptcha-response")
    driver.execute_script("arguments[0].innerText = {}".format(fetch.token('http://127.0.0.1:5000/www.supremenewyork.com/token')), element)

    done = input("Stop Tasks?[y or n] ")

    if done == "y":
        driver.close()

# if __name__ == '__main__':
    # kw = input("Enter Keywords: ")
    # negkw = input("Enter Negative Keywords: ")
    # kw = getKeywords(kw)
    # negkw = getKeywords(negkw)

    # webInfo = checkStock(kw, negkw)
    # item = webInfo[0]
    # category = webInfo[1]
driver = webdriver.Chrome('driver/chromedriver')
    # threading.Thread(target=task()).start()
    # threading.Thread(target=harvester()).start()

runTask = threading.Thread(target=task)
harvest = threading.Thread(target=createHarvest)

harvest.start()
runTask.start()
    # harvester()

        # load chrome
    # driver = webdriver.Chrome('driver/chromedriver')
    #
    # driver.get("https://www.supremenewyork.com/shop/all/" + category)
    # # order()
    # init = time.time()
    # order(item)
    # final = time.time()
    # el = final - init
    # print(el)

    # done = input("Stop Tasks?[y or n] ")


    # token = fetch.token('http://127.0.0.1:5000/www.supremenewyork.com/token')
    # print('Token:', token)

    # if done == "y":
    #     driver.close()


    # print('test')

