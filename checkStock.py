import requests
from bs4 import BeautifulSoup as bs
import json

def checkStock(kw, negkw):
    url = "https://www.supremenewyork.com/mobile_stock.json"
    # r = requests.get(url)
    response = requests.get(url, headers={'User-Agent': 'Mozilla'})
    response.encoding = 'utf-8'
    response.raise_for_status()
    # access JSOn content
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
    # kw = ["black", "ark"]
    kw = "black, ark"
    negkw = "sweatshirt, jacket, shirt"
    # kw = input("Enter Keywords: ")
    # negkw = input("Enter Negative Keywords: ")
    kw = getKeywords(kw)
    negkw = getKeywords(negkw)

    # itemName = checkStock(kw, negkw)[0]
    print(checkStock(kw, negkw))
