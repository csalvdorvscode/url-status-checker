import requests

with open("urls.txt", "r") as file:
    urls = list(set(file.readlines()))

for url in urls:
    url = url.strip()
    response = requests.get(url)
    print(url, response.status_code)
    try:
        response = requests.get(url, timeout=5)
        print(url, response.status_code)
    except request.exceptions.RequestException as e:
        print(url, "ERROR:" , e)



