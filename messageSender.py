from telethon.sync import TelegramClient 
from telethon.tl.types import PeerUser
import time
from datetime import datetime
import pytz


client = TelegramClient('Mustafamordaa', 11997410, '8fd90e8e2b6c41e74367798c9efa5aba' ) 
client.start() 

while True :
	tz = pytz.timezone('UTC')
	datetime = datetime.now(tz)
	Htm = datetime.strftime("%H")
	myHtm = int(Htm) + 3 
	if myHtm == 4 : 
		client.send_message(PeerUser(user_id=2042093845), "يسعد صباحك أستاذ")
		time.sleep(10)