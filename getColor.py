from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs



def colorOptions(item, color, category):
    if category == "Tops/Sweaters":
        category = "tops_sweaters"
    elif category == "T-Shirts":
        category = "t-shirts"

    url = "https://www.supremenewyork.com/shop/all/" + category

    response = requests.get(url, headers={'User-Agent': 'Mozilla'})
    response.encoding = 'utf-8'

    html = bs(response.text, 'html.parser')

    products = html.find_all('div', attrs={'class': 'product-name'})
    colors = html.find_all('div', attrs={'class': 'product-style'})

    possible = []
    colorOpt = []
    for i in range(0, len(products)):
        if products[i].get_text() == item:
            possible.append(products[i])
            colorOpt.append(colors[i])

    realColor = ""
    for i in colorOpt:
        if color in i.get_text().split():
            realColor = i
            break

    # test = realColor.split('"')
    prodUrl = str(realColor).split('"')[5]
    return prodUrl


def checkStock(kw, negkw):
    url = "https://www.supremenewyork.com/mobile_stock.json"
    # r = requests.get(url)
    response = requests.get(url, headers={'User-Agent': 'Mozilla'})
    response.encoding = 'utf-8'
    response.raise_for_status()
    # access JSON content
    jsonResponse = response.json()


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

if __name__ == "__main__":
    kw = input("Enter Keywords: ")
    negkw = input("Enter Negative Keywords: ")
    color = input("Color: ")

    kw = getKeywords(kw)
    negkw = getKeywords(negkw)

    webInfo = checkStock(kw, negkw)

    item = webInfo[0]
    category = webInfo[1]
    print(item, category)
    url = colorOptions(item, color.capitalize(), category)
    print(url)


    # done = input("Stop Tasks?[y or n] ")
    # if done == "y":
    #     driver.close()