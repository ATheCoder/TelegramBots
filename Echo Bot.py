import sys
import time
import telepot
from telepot.loop import MessageLoop

msg2={}
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    global msg2
    msg2=msg
    print(content_type)
    print(msg2)
    if content_type == 'photo':
        bot.sendMessage(chat_id,'Without caption :')
        bot.sendPhoto(chat_id, msg['photo'][len(msg['photo']) - 1]['file_id'])
        if 'caption' in msg:
            bot.sendMessage(chat_id, 'With caption :')
            bot.sendPhoto(chat_id, msg['photo'][len(msg['photo']) - 1]['file_id'],msg['caption'])
    elif content_type == 'video':
        bot.sendMessage(chat_id, 'Without caption :')
        bot.sendVideo(chat_id, msg['video'][len(msg['video']) - 1]['file_id'])
        if 'caption' in msg:
            bot.sendMessage(chat_id, 'With caption :')
            bot.sendVideo(chat_id, msg['video'][len(msg['video']) - 1]['file_id'],msg['caption'])
    elif content_type == 'audio':
        bot.sendMessage(chat_id, 'Without caption :')
        bot.sendAudio(chat_id,msg['audio']['file_id'])
        if 'caption' in msg:
            bot.sendMessage(chat_id, 'With caption :')
            bot.sendAudio(chat_id, msg['audio']['file_id'],msg['caption'])
    elif content_type == 'document':
        bot.sendMessage(chat_id, 'Without caption :')
        bot.sendDocument(chat_id, msg['document']['file_id'])
        if 'caption' in msg:
            bot.sendMessage(chat_id, 'With caption :')
            bot.sendDocument(chat_id, msg['document']['file_id'],msg['caption'])
    elif content_type == 'text':
        if msg['text']!='/start':
            bot.sendMessage(chat_id,msg['text'])
        else:
            bot.sendMessage(chat_id,'Forward a text or file or video or voice or photo to remove sender name and caption')
    elif content_type == 'voice':
        bot.sendVoice(chat_id,msg['voice']['file_id'])
    elif content_type == 'sticker':
        bot.sendSticker(chat_id,msg['sticker']['file_id'])
bot = telepot.Bot('351331662:AAEunXJ34Touv_CCTyNf2ff3w3zT9W1_3hM')
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
