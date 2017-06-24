/*
  KittyBot
  Shows random Kitty pictures and gifs.
*/

const TeleBot = require('telebot');
const bot = new TeleBot('390012609:AAHgq4ATgajR_RDD7WKKF0O9UmJRbC9_rgo');
const exec = require('child_process').exec;
a = 1;
b = 1;
// Great API for this bot
const API = 'https://thecatapi.com/api/images/get?format=src&type=';

function updateTime(chatId, messageId, tell) {

    bot.editMessageText(
            {chatId, messageId}, tell,
            {parseMode: 'html'}
        )

}


// Command keyboard
const replyMarkup = bot.keyboard([
    ['/kitty', '/kittygif']
], {resize: true, once: false});

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

// On command "start" or "help"
bot.on(['/start', '/help'], function (msg) {

    return bot.sendMessage(msg.chat.id,
        '😺 Use commands: /kitty, /kittygif and /about ' + msg.text, {replyMarkup}
    );

});

// On command "about"
bot.on('/about', function (msg) {

    let text = '😽 This bot is powered by TeleBot library ' +
        'https://github.com/kosmodrey/telebot Go check the source code!';

    return bot.sendMessage(msg.chat.id, text);

});

// On command "kitty" or "kittygif"
bot.on(['/kitty', '/kittygif'], function (msg) {

    let promise;
    let id = msg.chat.id;
    let cmd = msg.text.split(' ')[0];

    // Photo or gif?
    if (cmd == '/kitty') {
        promise = bot.sendPhoto(id, API + 'jpg', {
            fileName: 'kitty.jpg',
            serverDownload: true
        });
    } else {
        promise = bot.sendDocument(id, API + 'gif#', {
            fileName: 'kitty.gif',
            serverDownload: true
        });
    }

    // Send "uploading photo" action
    bot.sendAction(id, 'upload_photo');

    return promise.catch(error => {
        console.log('[error]', error);
        // Send an error
        bot.sendMessage(id, `😿 An error ${ error } occurred, try again.`);
    });

});

// Start getting updates
bot.start();
