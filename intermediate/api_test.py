# API (Application Programmable Interface)

import requests
import json

class API:
    def get_api_data(self):
        demo_url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url=demo_url)
        return response.json()
    
    def api_weather(self,city):
        url = f"https://wttr.in/{city}"
        response = requests.get(url)
        print(response.text)
        


api_a = API()
api_a.api_weather("New York")