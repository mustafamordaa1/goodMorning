from telethon.sync import TelegramClient 
from telethon.tl.types import PeerUser
import time
from datetime import datetime
import pytz

api_id = ""
api_hash = ""

#initializing the Telegram client
client = TelegramClient('SomeName', api_id, api_hash ) 
client.start() 

receiver_id = "get this id from telegram"
while True :
	#formatting the time.
	tz = pytz.timezone('Egypt')
	datetime = datetime.now(tz)
	Hours = datetime.strftime("%H")
	Mins = datetime.strftime("%M")
	
	#sets the message to be sent at 10 AM.
	if Hours == 10 :
		client.send_message(PeerUser(user_id= receiver_id), "your message")
		time.sleep(60)
