from sense_hat import SenseHat
import requests

sense = SenseHat()

ifttt_webhook_url = 'https://maker.ifttt.com/trigger/{}/with/key/cByhjCUEILFL022WIX_nLV'

r = (255, 0, 0)
g = (0, 255, 0)
y = (255, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)

home = [
    k, k, y, k, k, y, k, k,
    k, k, k, k, k, k, k, k,
    k, k, k, k, k, k, k, k,
    b, k, k, k, k, k, k, b,
    k, k, y, k, k, y, k, k,
    g, k, k, k, k, k, k, r,
    g, k, k, k, k, k, k, r,
    g, k, k, b, b, k, k, r
]

def post_ifttt_webhook(event, value1, value2):
    data = {'value1': value1, 'value2': value2}
    ifttt_event_url = ifttt_webhook_url.format(event)
    requests.post(ifttt_event_url, json=data)

def openFrontDoor():
    sense.set_pixel(0, 5, 0, 255, 0)
    sense.set_pixel(0, 6, 0, 255, 0)
    sense.set_pixel(0, 7, 0, 255, 0)
    post_ifttt_webhook('joystick_pushed', action, direction)


def closeFrontDoor():
    sense.set_pixel(0, 5, 255, 0, 0)
    sense.set_pixel(0, 6, 255, 0, 0)
    sense.set_pixel(0, 7, 255, 0, 0)

def openBackDoor():
    sense.set_pixel(7, 5, 0, 255, 0)
    sense.set_pixel(7, 6, 0, 255, 0)
    sense.set_pixel(7, 7, 0, 255, 0)
    
def closeBackDoor():
    sense.set_pixel(7, 5, 255, 0, 0)
    sense.set_pixel(7, 6, 255, 0, 0)
    sense.set_pixel(7, 7, 255, 0, 0)

try:
    sense.set_pixels(home)
    sense.stick.direction_up = openFrontDoor
    sense.stick.direction_down = closeFrontDoor



except:
    exit()

while True:
    for event in sense.stick.get_events():
        action = format(event.action)
        direction = format(event.direction)
    pass
