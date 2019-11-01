import requests
from retry import retry

@retry(tries=3)
def do_request():
    response = requests.get("http://localhost:5000/")
    response.raise_for_status()
    print(response.text)

do_request()