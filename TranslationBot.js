
const TeleBot = require('telebot');
const bot = new TeleBot('384552644:AAGllMEVTpKFdMULJ9VRTwAF55ieGvQqWK4');
const translate = require('google-translate-api');

// Log every text message
bot.on('text', function (msg) {
	translate(msg.text, {to: 'fa'}).then(res => {
    bot.sendMessage(msg.chat.id, res.text)
    console.log(res.from.language.iso);
}).catch(err => {
    console.error(err);
});
});


// Start getting updates
bot.start();
