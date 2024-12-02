from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Добро пожаловать в FlowerDelivery Bot!")

def notify_order(update: Update, context: CallbackContext):
    update.message.reply_text("Ваш заказ отправлен на доставку.")

updater = Updater("YOUR_BOT_TOKEN")
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
