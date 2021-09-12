import random
import requests
import time
while True:
    UCID = random.choice(['A3E59','P8D7Q'])
    gaz = random.randint(0,100)
    water_lvl = random.randint(0,100)
    water_temp = random.randint(80,85)
    water_press = random.randint(0,100)
    speed = random.randint(1200,1900)
    oil_lvl = random.randint(0,100)
    oil_temp = random.randint(80,100)
    oil_press = random.randint(42,61)

    requests.post("http://192.168.186.107:5000/api/v1/data/",json={
        "device": UCID,
        "gaz": gaz,
        "water_lvl": water_lvl,
        "water_temp": water_temp,
        "water_press": water_press,
        "speed": speed,
        "oil_lvl": oil_lvl,
        "oil_temp": oil_temp,
        "oil_press": oil_press
    })
    requests.post("http://192.168.186.107:5000/api/v1/info/",json={
        "device": UCID,
        "gaz": gaz,
        "water_lvl": water_lvl,
        "water_temp": water_temp,
        "water_press": water_press,
        "speed": speed,
        "oil_lvl": oil_lvl,
        "oil_temp": oil_temp,
        "oil_press": oil_press
    })
    time.sleep(1)


# UCID = random.choice(['A3E59','P8D7Q'])
# gaz = random.randint(0,100)
# water_lvl = random.randint(0,100)
# water_temp = random.randint(80,85)
# water_press = random.randint(0,100)
# speed = random.randint(1200,1900)
# oil_lvl = random.randint(0,100)
# oil_temp = random.randint(80,100)
# oil_press = random.randint(42,61)

# res = requests.post("http://192.168.186.107:5000/api/v1/data/",json={
#     "device": UCID,
#     "gaz": gaz,
#     "water_lvl": water_lvl,
#     "water_temp": water_temp,
#     "water_press": water_press,
#     "speed": speed,
#     "oil_lvl": oil_lvl,
#     "oil_temp": oil_temp,
#     "oil_press": oil_press
# })
# print(res.status_code)