import requests

BASE = "http://127.0.0.1:5000/"

data=[{"name": "MrBeast", "views": 36460, "likes": 16560},
      {"name": "Carry", "views": 33640, "likes": 1043},
      {"name": "BB Ki Vines", "views": 3263630, "likes": 13464},
      {"name": "Amit", "views": 3515450, "likes": 1450}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response.json())

response=requests.delete(BASE + "video/3")
print(response)


input("Press Enter ")
response = requests.get(BASE + "video/3")
print(response.json())


#response = requests.post(BASE + "helloworld")
#print(response.json())
