import threading
import requests

def call():
    response = requests.get('http://localhost:8080/')
    print(response.json())
    print("----------------------------------------")


def use_threading():
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=call)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

use_threading()
