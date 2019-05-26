import logging

from random import randrange
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def hello(update, context):
    message = ( "Приветики малыши, это долгожданный Минюнька бот.\n"
                "Пока что тока мемасики (бета версия сюк).\n"
                "Улучшения каждую неделю.\n"
                "Донатьте денюшку => будут остальные плюшки." )
    update.message.bot.send_message(update.message.chat.id, message)


def send_mem(update, context):
    arg_num = len(context.args)
    if arg_num == 0:
        mem_id = randrange(0, 10000)
        mem_link = 'https://t.me/Tt4ch/' + str(mem_id)
        print(mem_link)
        update.message.bot.send_photo(update.message.chat.id, mem_link)
        #update.message.reply_photo(mem_link)
    elif arg_num == 1:
        mem_num = int(context.args[0])
        if mem_num >= 1 and mem_num <= 10:
            mem_ids= [randrange(0, 10000) for p in range(0, mem_num)]
            for curr_mem_id in mem_ids:
                mem_link = 'https://t.me/Tt4ch/' + str(curr_mem_id)
                print(mem_link)
                try:
                    update.message.bot.send_photo(update.message.chat.id, mem_link)
                except:
                    update.message.bot.send_message(update.message.chat.id, "Хуевая ссылочка")
                    pass
        elif mem_num > 10:
            update.message.bot.send_message(update.message.chat.id, "Не охуел малыш? Мемный передоз ни кому не нужен")
        else:
            update.message.bot.send_message(update.message.chat.id, "Идешь нахуй шутник")
    else:
        update.message.bot.send_message(update.message.chat.id, "Нахуй идешь - Миниме не проведешь")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("734904187:AAG5BdpLPI1FSjQnlVXZzTFQQiQsl7vZKIo", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    greeting_handler = CommandHandler('hello', hello)
    sendmem_handler = CommandHandler('mem', send_mem, pass_args=True)
    dp.add_handler(greeting_handler)
    dp.add_handler(sendmem_handler)
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
