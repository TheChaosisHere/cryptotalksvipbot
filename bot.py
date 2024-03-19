from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_API_TOKEN' with your actual Telegram API token
TOKEN = '7147527120:AAHJw10WvLSEOYZGI1lvayJ75ORC3AFuzaY'

# Replace 'YOUR_CHAT_ID' with your chat ID where you want to receive forwarded messages
ADMIN_CHAT_ID = '1847722399'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to CryptoTalksVIP! To get started, please reply to this message with your UID ')

def forward_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.text
    if user_id.isdigit():  # Check if the message contains only digits
        user_details = f"User: @{update.effective_user.username}" if update.effective_user.username else f"User ID: {update.effective_user.id}"
        forwarded_message = f"Forwarded from: {user_details}\n\n{user_id}"
        context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=forwarded_message)
        
        # Send confirmation message to the user
        update.message.reply_text('\nThanks for your interest!\nAfter reviewing your UID, we’ll send an invite if you’re eligible and used our referral code.\nStay tuned!')
    else:
        update.message.reply_text('Please send only Exchange UID Here')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
