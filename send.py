# yes this is VERYYYYY basic, just for a first post :)

import requests

webhook = "webhook url" # change to the discord webhook url

data = {
    "content": "this is a test message, change to whatever you wanna send over the webhook." # change to message thats being sent over the webhook
}

requests.post(webhook, data=data) # send post request to webhook url containing the message data

print("Message Has Been Sent To The Webhook") # print that the message has been sent
