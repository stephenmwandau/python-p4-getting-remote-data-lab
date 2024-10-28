import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response_body = requests.get(self.url).content
        return response_body

    def load_json(self):
        byte_response = self.get_response_body()
        byte_response_string = byte_response.decode('utf-8')
        json_response = json.loads(byte_response_string)
        print(f'{json_response}')
        return json_response

request1 = GetRequester(url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")

request1.load_json()