from email.quoprimime import body_check
from PIL import Image
import requests
import base64

r = requests.post('https://iot-door-lock-system.herokuapp.com/changedoorstate', json={
    "msg": "YES"
})
print(r.text)
