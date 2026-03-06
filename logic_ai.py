import json
import requests
import time
from config import *

api_key = "e5456b6b-1345-4bba-876d-36f12242d854"
authorization = "Bearer %s" % api_key

class LeonardoAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.authorization = "Bearer %s" % api_key

        self.headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": self.authorization
        }
        self.url = "https://cloud.leonardo.ai/api/rest/v1/generations"
    def generate_image(self, prompt, filename="result.jpg"):
        payload = {
        "height": 512,
        "width": 512,
        "modelId": "ca0be369-b36e-4726-bca9-3bb524ffa6a7",
        "prompt": prompt
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        print(response.status_code)
        generation_id = response.json()['sdGenerationJob']['generationId']
        time.sleep(20)
        result_url = "https://cloud.leonardo.ai/api/rest/v1/generations/%s" % generation_id
        response = requests.get(result_url, headers=self.headers)
        data = response.json()
        image_url = data["generations_by_pk"]["generated_images"][0]["url"]
        image_data = requests.get(image_url).content

        # Сохраняем изображение в файл
        with open(filename,"wb") as file:
            file.write(image_data)
        return image_url

api = LeonardoAPI(API_Token)

if __name__ == "__main__":
    api.gen_image("An oil painting of a cat", "image.jpg")
    print("Yes")