import requests

class Util():
    def __init__(self):
        self.URL = "https://reqres.in"
        
util = Util()

def get_users():
    url = f"{util.URL}/api/users"

    header = {"accept": "application/json"}

    r = requests.get(url=url, headers=header)

    print(r.status_code)
    print(r.json()["data"][0]["id"])
    print(r.json()["data"][0]["email"])

if __name__ == "__main__":
    get_users()