import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
wait_room=[]
battle={}
time_played={}
selected_option={}
score={}
first_name={}
last_name={}
username={}
arr=["ROCK","PAPER","SCISSORS","LIZZARD","SPOCK"]

def read_from_file():
    dict_names = {}
    f = open(r"C:\Users\Mahdi\Desktop\file.txt", "r")
    for line in f.readlines():
        dic={}
        x = line.find(" ")
        user_id = line[0:x]
        y = line.find( " " , x + 1)
        score = line[x+1:y]
        name = line[y + 1:]
        if name.find('\n')==-1:
            dic['name']=name
        else:
            dic['name']=name[:len(name)-1]
        dic['score']=int(score)
        dict_names[str(user_id)]=dic
    return dict_names
def game_result(first,last):
    if first == "1":
        if last == "2":
            return -1
        elif last == "3":
            return 1
        elif last=="4":
            return 1
        elif last=="5":
            return -1
        else:
            return 0
    if first == "2":
        if last == "1":
            return 1
        elif last == "3":
            return -1
        elif last=="4":
            return -1
        elif last=="5":
            return 1
        else:
            return 0
    if first == "3":
        if last == "1":
            return -1
        elif last == "2":
            return 1
        elif last=="4":
            return 1
        elif last=="5":
            return -1
        else:
            return 0
    if first == "4":
        if last == "1":
            return -1
        if last == "2":
            return 1
        elif last == "3":
            return -1
        elif last=="5":
            return 1
        else:
            return 0
    if first == "5":
        if last == "1":
            return 1
        if last == "2":
            return -1
        elif last == "3":
            return 1
        elif last=="4":
            return -1
        else:
            return 0
keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Rock ✊🏻', callback_data='1'),InlineKeyboardButton(text='Paper 🤚🏻', callback_data='2')],
                                                 [InlineKeyboardButton(text='Scissors ✌🏻', callback_data='3'),InlineKeyboardButton(text='Lizard 👌🏻', callback_data='4')],[InlineKeyboardButton(text='Spock 🖖🏻', callback_data='5')]
                                                 ])
def write_to_file(dictt):
    f = open(r"C:\Users\Mahdi\Desktop\file.txt", "w")
    for key in dictt:
        f.write(key+" ")
        f.write(str(dictt[key]['score'])+" ")
        f.write(dictt[key]['name']+"\n")
    f.close()

diction = read_from_file()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type=='text':
        if 'username' in msg['from']:
            username[chat_id] = msg['from']['username']
        else:
            if 'last_name' in msg['from']:
                username[chat_id] = msg['from']['first_name'] + msg['from']['last_name']
            else:
                username[chat_id] = msg['from']['first_name']
        if str(chat_id) not in diction:
            print("hi")
            dicss={}
            dicss['name'] = username[chat_id]
            dicss['score'] = 0
            diction[str(chat_id)] = dicss
            write_to_file(diction)

        print(str(chat_id)+" "+username[chat_id]+" : "+msg['text'])
        first_name[chat_id]=msg['from']['first_name']
        if chat_id in battle:
            if msg['text'] == "/concede":
                if chat_id in wait_room:
                    del wait_room[chat_id]
                diction[str(chat_id)]['score'] -= 5
                diction[str(battle[chat_id])]['score'] += 2
                bot.sendMessage(chat_id, "You lose this game ...\n")
                bot.sendMessage(battle[chat_id], msg['from']['first_name'] + " conceded from the game so you are the winner\nPress /start to start a new game ")
                del score[battle[chat_id]]
                del score[chat_id]
                del time_played[battle[chat_id]]
                del time_played[chat_id]
                del battle[battle[chat_id]]
                del battle[chat_id]
                write_to_file(diction)
            elif msg['text'] == "/help":
                bot.sendMessage(chat_id,"I suggest you to see my profile picture or see this video : http://yon.ir/NGJqz")
            else:
                bot.sendMessage(chat_id,"Dont send message without reason idiiot ...\nOnly Commands are acceptable")
        else:
            if msg['text'] == "/start":
                if len(wait_room)==0:
                    wait_room.append(chat_id)
                    bot.sendMessage(chat_id, 'Wait until someone joins...')
                else:
                    if chat_id!=wait_room[0]:
                        battle[chat_id]=wait_room[0]
                        battle[wait_room[0]]=chat_id
                        time_played[chat_id]=0
                        time_played[wait_room[0]]=0
                        score[chat_id]=0
                        score[wait_room[0]]=0
                        bot.sendMessage(chat_id, "You're lucky I found someone :)")
                        bot.sendMessage(wait_room[0], "You're lucky I found someone :)")
                        bot.sendMessage(chat_id,"⚔️⚔️  "+username[chat_id]+'   VS   '+username[wait_room[0]]+"  ⚔️⚔️" )
                        bot.sendMessage(wait_room[0],"⚔️⚔️  "+username[chat_id]+'   VS   '+username[wait_room[0]]+"  ⚔️⚔️" )
                        bot.sendMessage(chat_id, 'Try your luck ...', reply_markup=keyboard)
                        bot.sendMessage(battle[chat_id], 'Try your luck ...', reply_markup=keyboard)
                        del wait_room[0]
                    else:
                        bot.sendMessage(chat_id,"Can you say me what are you doing ?\nWait until someone join\nOk ??")
            elif msg['text'] == "/help":
                bot.sendMessage(chat_id, "I suggest you to see my profile picture or see this video : http://yon.ir/NGJqz")
            elif msg['text'] == "/concede":
                if chat_id in wait_room:
                    del wait_room[0]
                    bot.sendMessage(chat_id,"Searching canceled")

                if chat_id in battle:
                    bot.sendMessage(chat_id, "You lost this game ...\n")
                    bot.sendMessage(battle[chat_id], msg['from'][
                        'first_name'] + " conceded from the game so you are the winner\nPress /start to start a new game ")
                    del score[battle[chat_id]]
                    del score[chat_id]
                    del time_played[battle[chat_id]]
                    del time_played[chat_id]
                    del battle[battle[chat_id]]
                    del battle[chat_id]
                write_to_file(diction)
            elif msg['text']=='/leaderboard':
                show=""
                sorted_name=[]
                sorted_scores=[]
                sorted_chat_id=[]
                for key in diction:
                    sorted_chat_id.append(key)
                    sorted_name.append(diction[key]['name'])
                    sorted_scores.append(diction[key]['score'])
                for i in range(0,len(sorted_scores)):
                    for j in range(i+1,len(sorted_scores)):
                        if sorted_scores[j]>sorted_scores[i]:
                            temp=sorted_scores[i]
                            temp_string=sorted_name[i]
                            temp_chat=sorted_chat_id[i]
                            sorted_scores[i]=sorted_scores[j]
                            sorted_name[i]=sorted_name[j]
                            sorted_chat_id[i]=sorted_chat_id[j]
                            sorted_scores[j]=temp
                            sorted_name[j]=temp_string
                            sorted_chat_id[j]=temp_chat
                for i in range(0,len(sorted_scores)):
                    if i==0:
                        show+="🥇 "+sorted_name[i]+"    :    "+str(sorted_scores[i])+"\n"
                    elif i==1:
                        show += "🥈 " + sorted_name[i] + "    :    " + str(sorted_scores[i]) + "\n"
                    elif i==2:
                        show += "🥉 " + sorted_name[i] + "    :    " + str(sorted_scores[i]) + "\n"
                    else:
                        show +="  "+str(i+1)+" - "+sorted_name[i] + "    :    " + str(sorted_scores[i]) + "\n"
                for i in range(0,len(sorted_chat_id)):
                    if str(chat_id)==sorted_chat_id[i]:
                        show +="\n---------------\nYour rank in the world  :    "+str(i+1)
                bot.sendMessage(chat_id,show)
            else:
                bot.sendMessage(chat_id, "Dont send message without reason idiiot ...\nOnly Commands are acceptable")
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print(msg['from']['first_name']+" : ",from_id," ---> ", query_data)
    if (time_played[from_id] - time_played[battle[from_id]] == 0):
        time_played[from_id] = time_played[from_id] + 1
    if (time_played[from_id] - time_played[battle[from_id]] == -1):
        time_played[from_id] = time_played[from_id] + 1
        
    selected_option[from_id] = query_data
    if time_played[from_id] == time_played[battle[from_id]]:
        if game_result(selected_option[from_id], selected_option[battle[from_id]]) == 1:
            bot.sendMessage(from_id, username[battle[from_id]] + ' Choose " ' + arr[int(selected_option[battle[from_id]]) - 1] + ' "')
            bot.sendMessage(battle[from_id],username[from_id] + ' Choose " ' + arr[int(selected_option[from_id]) - 1] + ' "')
            score[from_id] = score[from_id] + 1
        elif game_result(selected_option[from_id], selected_option[battle[from_id]]) == -1:
            bot.sendMessage(from_id, username[battle[from_id]] + ' Choose " ' + arr[int(selected_option[battle[from_id]]) - 1] + ' "')
            bot.sendMessage(battle[from_id],username[from_id] + ' Choose " ' + arr[int(selected_option[from_id]) - 1] + ' "')
            score[battle[from_id]] = score[battle[from_id]] + 1
        if game_result(selected_option[from_id], selected_option[battle[from_id]]) == 0:
            bot.sendMessage(from_id, username[battle[from_id]] + ' Choose " ' + arr[int(selected_option[battle[from_id]]) - 1] + ' "')
            bot.sendMessage(battle[from_id],username[from_id] + ' Choose " ' + arr[int(selected_option[from_id]) - 1] + ' "')
        bot.sendMessage(from_id, "🛑🛑  You : " + str(score[from_id]) + "\n\n🛑🛑  " + username[battle[from_id]] + " : " + str(score[battle[from_id]]))
        bot.sendMessage(battle[from_id],"🛑🛑  You : " + str(score[battle[from_id]]) + "\n\n🛑🛑  " + username[from_id] + " : " + str(score[from_id]))
        if score[from_id] == 5:
            diction[str(from_id)]['score'] +=   score[from_id] - score[battle[from_id]]
            diction[str(battle[from_id])]['score'] += score[battle[from_id]] - score[from_id]
            write_to_file(diction)
            bot.sendMessage(from_id, "You win\nPress /start to start a new game ")
            bot.sendMessage(battle[from_id],"You lost\nPress /help to learn how to play. noob !\nPress /start to start a new game ")
            del score[battle[from_id]]
            del score[from_id]
            del time_played[battle[from_id]]
            del time_played[from_id]
            del first_name[from_id]
            del first_name[battle[from_id]]
            del battle[battle[from_id]]
            del battle[from_id]
        elif score[battle[from_id]] == 5:
            diction[str(battle[from_id])]['score'] += score[battle[from_id]] - score[from_id]
            diction[str(from_id)]['score'] += score[from_id] - score[battle[from_id]]
            write_to_file(diction)
            bot.sendMessage(battle[from_id], "You win\nPress /start to start a new game ")
            bot.sendMessage(from_id, "You lost\nPress /help to learn how to play. noob !\nPress /start to start a new game ")
            del score[battle[from_id]]
            del score[from_id]
            del time_played[battle[from_id]]
            del time_played[from_id]
            del first_name[from_id]
            del first_name[battle[from_id]]
            del battle[battle[from_id]]
            del battle[from_id]
        else:
            bot.sendMessage(from_id, 'Try your luck ...', reply_markup=keyboard)
            bot.sendMessage(battle[from_id], 'Try your luck ...', reply_markup=keyboard)
    bot.answerCallbackQuery(query_id, arr[int(query_data)-1])
bot = telepot.Bot('375880514:AAHYHQea8YqJUxN87MxBQP9vFyMMFMzI5Mw')
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')
while 1:
    time.sleep(10)
    print("\n")
    print("-------------------------------------------")
    print("battle arena : ",battle)
    print("waiting room  : ", wait_room)
    print("Scores : ",score)
    print("time_played  : ", time_played)
    print("Dictionary : ",diction)
    print("-------------------------------------------")