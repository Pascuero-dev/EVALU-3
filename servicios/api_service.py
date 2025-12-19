import urllib.request
import urllib.error
import json

class ApiService:
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    def get_posts(self):
        try:
            with urllib.request.urlopen(self.BASE_URL) as response:
                if response.status == 200:
                    return json.loads(response.read().decode())
        except urllib.error.URLError as e:
            print(f"Error GET: {e}")
            return []

    def post_data(self, data):
        try:
            json_data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(self.BASE_URL, data=json_data, headers={'Content-Type': 'application/json'}, method='POST')
            with urllib.request.urlopen(req) as response:
                print(f"Estado API POST: {response.status}") # Debe ser 201
                return json.loads(response.read().decode())
        except urllib.error.URLError as e:
            print(f"Error POST: {e}")

    def put_data(self, id_obj, data):
        url = f"{self.BASE_URL}/{id_obj}"
        try:
            json_data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=json_data, headers={'Content-Type': 'application/json'}, method='PUT')
            with urllib.request.urlopen(req) as response:
                 print(f"Estado API PUT: {response.status}") # Debe ser 200
        except urllib.error.URLError as e:
            print(f"Error PUT: {e}")

    def delete_data(self, id_obj):
        url = f"{self.BASE_URL}/{id_obj}"
        try:
            req = urllib.request.Request(url, method='DELETE')
            with urllib.request.urlopen(req) as response:
                print(f"Estado API DELETE: {response.status}") # Debe ser 200
        except urllib.error.URLError as e:
            print(f"Error DELETE: {e}")