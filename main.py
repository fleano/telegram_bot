from telegram.ext import updater
import Constants as keys
from telegram.ext import *
import Responses as R
from libdw import pyrebase

print('Bot started...')

projectid = "myctdproject-f34ea-default-rtdb.asia-southeast1"
dburl = "https://" + projectid + ".firebasedatabase.app"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyBeAz9pXS01ryw2B_u-WeusKigtnrL77_g"
email = "justinlooijw@gmail.com"
password = "test012"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
user = auth.refresh(user['refreshToken'])

key = 'telegramBot'


def start_command(update, context):
    update.message.reply_text(
        "Hello! I am Justin's first bot. I was created to quickly give out information about SUTD Modelling Space and Systems Module")


def help_command(update, context):
    update.message.reply_text(
        'If you need help! You should ask for it on Google! You can also go to this url: https://www.sutd.edu.sg/Admissions/Undergraduate/Unique-Curriculum/Freshmore-Subjects/Modelling-Space-and-Systems')


def say_command(update, context):
    text = str(update.message.text)
    text = text.replace('/say', '')
    update.message.reply_text(text)


def store_command(update, context):
    text = str(update.message.text)
    text = text.replace('/store', '')
    if type(text) == str:
        db.child(key).set(text, user['idToken'])
        update.message.reply_text('Command completed')


def get_command(update, context):
    node = db.child(key).get(user['idToken'])
    value = node.val()
    if type(value) == str:
        update.message.reply_text(value)


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler('say', say_command))
    dp.add_handler(CommandHandler('store', store_command))
    dp.add_handler(CommandHandler('get', get_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
