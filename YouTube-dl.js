/*
  KittyBot
  Shows random Kitty pictures and gifs.
*/

const TeleBot = require('telebot');
const bot = new TeleBot('390012609:AAHgq4ATgajR_RDD7WKKF0O9UmJRbC9_rgo');
const exec = require('child_process').exec;
a = 1;
b = 1;

function updateTime(chatId, messageId, tell) {

    bot.editMessageText(
            {chatId, messageId}, tell,
            {parseMode: 'html'}
        )

}


// Command keyboard

// Log every text message
bot.on('text', function (msg) {
    var lel = false;
    console.log(`[text] ${ msg.chat.id } ${ msg.text }`);
    child = exec('youtube-dl --cookies outputfile.txt ' + msg.text,
    function (error, stdout, stderr) {
        lel = false;
        newChild = exec('youtube-dl --cookies outputfile.txt --get-filename ' + msg.text, function (err, out, serr){
            bot.sendMessage(msg.chat.id, "http://46.101.74.34/downloads/" + encodeURIComponent(out.trim()))
        });
        if (error !== null) {
            console.log('exec error: ' + error);
        }
});
    child.stdout.on('data', function(data) {
        if(!lel){
            lel = true;
        return bot.sendMessage(msg.chat.id, data).then(re => {
            child.stdout.on('data', function(data){
                updateTime(msg.from.id, re.result.message_id, data);
            })
        })
        }
});
});


// Start getting updates
bot.start();
