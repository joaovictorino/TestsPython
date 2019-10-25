import requests
from retry import retry

@retry()
def do_request(service):
    response = requests.get(service)
    response.raise_for_status()
    return response.text

def what_is_my_ip():
    result = do_request("http://localhost:5000/")
    print(result)

what_is_my_ip()