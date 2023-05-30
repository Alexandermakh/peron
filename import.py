import requests
import sys

sys.setrecursionlimit(5500)

products = 0 # примерный подсчет импортированных товаров
q = 100 # шаг импортера (сколько товаров обрабатывается за 1 запрос)

qw = False
qw_url = 'false'
def makeRequest(scrl):
    global products
    global qw
    global qw_url
    products = products + 1
    print("NEW REQUEST")
    # Ссылка на файл cron_update.php
    url = 'https://peron-group.ru/test.php?scrl=' + scrl +'&token=5098587596&next=' + qw_url

    r = requests.get(url, verify=False)

    if r.text != 'done':
        print("REQUESTS: ", products)
        print("PRODUCTS: ", (products * q))
        print("MAKING NEW REQUEST")
        print(r.text)
        makeRequest(r.text)
    else:
        if not qw:
            print("\n\n\n\n\n NEXT!!!!!!!!!!!!!!!!!!\n\n\n\n\n")
            qw = True
            qw_url = 'true'
            makeRequest('')
        print("REQUESTS: ", products)
        print("PRODUCTS: ", (products * q))
        print("SUCCESS")
        return True

makeRequest('')
