import requests
import time

target = input("Digite a URL: ")

while True:
    try:
        # GET
        r = requests.get(target)
        print("GET:", r.status_code)

    except Exception as e:
        print("Erro:", e)

    # time.sleep(3) 
