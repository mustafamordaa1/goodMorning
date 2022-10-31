from telethon.sync import TelegramClient 
from telethon.tl.types import PeerUser
import time
from datetime import datetime
import pytz

#initializing the Telegram client
client = TelegramClient('Mustafamordaa', 11997410, '8fd90e8e2b6c41e74367798c9efa5aba' ) 
client.start() 

while True :
	tz = pytz.timezone('UTC')
	datetime = datetime.now(tz)
	Htm = datetime.strftime("%H")
	Mtm = datetime.strftime("%M")
	myHtm = int(Htm) + 3 
	if int(Mtm) % 10 == 0 : 
		client.send_message(PeerUser(user_id=5244946853), "قومي جلي")
		time.sleep(60)
