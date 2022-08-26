from email.quoprimime import body_check
from PIL import Image
import requests
import base64
with open("C:\git_git\Mypc\project\IOT\send\gojo.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

url = 'https://iot-door-lock-system.herokuapp.com/send'

r = requests.post('https://iot-door-lock-system.herokuapp.com/send', json={
    "Id": 78912,
    "Customer": "Jason Sweet",
    "Quantity": 1,
    "Price": 18.00,
    "file": my_string.decode("utf-8")
})
print(r.text)
