import requests
import time
import datetime

def findStock():
    # url = "https://www.supremenewyork.com/mobile_stock.json"

    url = "https://kith.com/products.json"
    response = requests.get(url, headers={'User-Agent': 'Mozilla'})
    response.encoding = 'utf-8'
    response.raise_for_status()
    jsonResponse = response.json()

    found = False
    print("New Products: ")
    newestItems = []
    lastItemSet = []
    repeat = False
    first = True


    while found == False:
        response = requests.get(url, headers={'User-Agent': 'Mozilla'})
        response.encoding = 'utf-8'
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()

        # newestItems = [i["name"] for i in jsonResponse["products_and_categories"]["new"]]
        newestItems = [i["title"] for i in jsonResponse["products"]]
        print(datetime.datetime.now().time())
        print(newestItems)


        if lastItemSet != newestItems and first == False:
            found = True


        first = False

        lastItemSet = newestItems
        time.sleep(1)


if __name__ == '__main__':
    findStock()