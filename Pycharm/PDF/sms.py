import os
from twilio.rest import Client
import random

otp = random.randint(1000,9000)

account_sid = "ACc49d4bb14f3391d56a70cd30b538886b"
auth_token = "9825de22cda7897220fc228dd2f2dec6"
# account_sid = 'AC596df635b0f29f5f336bae3eb5efc32f'
# auth_token = '6d55b52e4f81ad7a948e6e8c83f3d553'
client = Client(account_sid, auth_token)

message = client.messages.create(body='your otp is '+str(otp),
                                 from_="+19896629343",
                                 to='+918744969547')
print('Done')
print(message.sid)
