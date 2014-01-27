import os
import time
import pifacedigitalio as piface
from twilio.rest import TwilioRestClient


account="xxxxxxxxxxxxxxx"
token="xxxxxxxxxxxxxx"
client = TwilioRestClient(account,token)
admin = "+1xxxxxxxx"

while(True):
    piface.init()
    if(piface.digital_read(0)==1):
        piface.digital_write(0,1)
        message = client.messages.create(to=admin,from_= "+1xxxxx", body = "Flood alert")
    else:
        piface.digital_write(0,0);
    time.sleep(10)
