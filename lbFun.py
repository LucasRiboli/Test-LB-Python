import requests
from itertools import cycle
import random

urls = ["http://localhost:5000", "http://localhost:5001", "http://localhost:5002", "http://localhost:5003"]


url_cycle = cycle(urls)

def round_robin_lb(request_path):
    """Round Robin Load Balancer"""
    target_url = next(url_cycle) + request_path
    try:
        response = requests.get(target_url)
        return f"Card: {response.content} // URL: {target_url}"
    except requests.RequestException as e:
        return str(e)

def random_lb(request_path):
    """Random Load Balancer"""
    target_url = random.choice(urls) + request_path
    try:
        response = requests.get(target_url)
        return f"Card: {response.content} // URL: {target_url}"
    except requests.RequestException as e:
        return str(e)

def lbFun(request_path, algorithm='round_robin'):
    """Load Balancer with Algorithm Selection"""
    if algorithm == 'round_robin':
        return round_robin_lb(request_path)
    elif algorithm == 'random':
        return random_lb(request_path)
    else:
        return "Unknown algorithm"

if __name__ == "__main__":
    for i in range(10):
        print("Round Robin:", lbFun("/", algorithm='round_robin'))
        print("Random:", lbFun("/", algorithm='random'))
