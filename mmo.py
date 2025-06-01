# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImlseWFzaDM2MzZAZ21haWwuY29tIiwicGFzc3dvcmRfY2hhbmdlZCI6IiJ9.9tHAn61K_kGhDgirCChttsm5TjLDU5YjV5WDWeIw1wM

# import requests
#
# url = "https://api.artifactsmmo.com/my/Keklik/action/move"
#
# payload = {
#     "x": 2,
#     "y": 0
# }
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImlseWFzaDM2MzZAZ21haWwuY29tIiwicGFzc3dvcmRfY2hhbmdlZCI6IiJ9.9tHAn61K_kGhDgirCChttsm5TjLDU5YjV5WDWeIw1wM",
#     "Connection": "close"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.json())

import requests
import time
#
# i = 0
#
# while i <= 10:
#
#     url = "https://api.artifactsmmo.com/my/Keklik/action/gathering"
#
#     headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImlseWFzaDM2MzZAZ21haWwuY29tIiwicGFzc3dvcmRfY2hhbmdlZCI6IiJ9.9tHAn61K_kGhDgirCChttsm5TjLDU5YjV5WDWeIw1wM"
#     # "Connection": "close"
#     }
#
#     response = requests.post(url, headers=headers)
#
#     print(response.json())
#
#     i += 1
#
#     print(f'Добыто руды: {i}')
#
#     time.sleep(27)

class Action:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImlseWFzaDM2MzZAZ21haWwuY29tIiwicGFzc3dvcmRfY2hhbmdlZCI6IiJ9.9tHAn61K_kGhDgirCChttsm5TjLDU5YjV5WDWeIw1wM"
        # "Connection": "close"
    }
    def move(self, x, y):
        url = "https://api.artifactsmmo.com/my/Keklik/action/move"
        payload = {
        "x": x,
        "y": y
        }
        response = requests.post(url, json=payload, headers=self.headers)

        print(response.json())


    def gathering(self, i):
        while i <= 10:
            url = "https://api.artifactsmmo.com/my/Keklik/action/gathering"
            response = requests.post(url, headers=self.headers)

            print(response.json())

            i += 1

            print(f'Добыто руды: {i}')

            time.sleep(30)

test = Action()
test.gathering(9)





