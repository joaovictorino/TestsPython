import requests
from retry import retry
from retry.api import retry_call

#annotation
#@retry(tries=3)
def do_request():
    response = requests.get("http://localhost:5000/")
    response.raise_for_status()
    print(response.text)

#annotation
#do_request()

#retry call method
retry_call(do_request, tries=4)