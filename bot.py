from telegram.ext import Updater, CommandHandler, ConversationHandler
from resources.credentials import credential
from resources.commands import start, help
from resources.documentCommands import doc, concept, element

if __name__ == '__main__':

    updater = Updater(token=credential, use_context=True)

    dispatch = updater.dispatcher

    dispatch.add_handler(CommandHandler('start', start))
    dispatch.add_handler(CommandHandler('help', help))
    dispatch.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('document', doc)
        ],
        states={
            'doc': [
                CommandHandler('concept', concept),
                CommandHandler('element', element),
            ]
        },
        fallbacks=[]
    ))

    updater.start_polling()
    print('starting bot')
    updater.idle()