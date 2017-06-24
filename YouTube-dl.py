import time
import subprocess
import telepot
from telepot.loop import MessageLoop
import random
bot = telepot.Bot('390012609:AAHgq4ATgajR_RDD7WKKF0O9UmJRbC9_rgo')
def handle(msg):
	print(msg)
	chat_id = msg['chat']['id']
	text = msg['text']
	if text == "/start":
		bot.sendMessage(chat_id, "You have Started the Bot! Now Enter the Desired URL.")
	else:
		bot.sendMessage(chat_id, "Proccesing your Request!")
		subprocess.call("youtube-dl --cookies outputfile.txt " + text, shell=True)
		done = "http://46.101.74.34/downloads/" + subprocess.check_output("youtube-dl --cookies outputfile.txt --get-filename " + text, shell=True)
		done = done.replace(' ', '%20')
		bot.sendMessage(chat_id, done)
MessageLoop(bot, handle).run_as_thread()
while 1:
	time.sleep(10)

