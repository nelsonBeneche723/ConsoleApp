
# Envoi de messages whatsapp
#from twilio.rest import Client
#import os
##instance de la classe Client
#client=Client()
#from_msg_number='whatsapp:+14155238886'
#to_whatsapp_number='whatsapp:'+os.environ['MY_PHONE_NUMBER']

##Creation de message
#client.messages.create(body='Bonjour Sony',from_=from_msg_number,to=to_whatsapp_number)

import urllib

# Please see the FAQ regarding HTTPS (port 443) and HTTP (port 80/5567)

url = "«EAPI URL»/submission/send_sms/2/2.0"

params = urllib.urlencode({'username' : 'myusername', 'password' : 'xxxxxxxx', 'message' : 'Testing Python', 'msisdn' : 271231231234})
f = urllib.urlopen(url, params)

s = f.read()

result = s.split('|')
statusCode = result[0]
statusString = result[1]
resul=result[2]
if statusCode != '0':
    print("echec")
else:
    print("russie")

f.close()

