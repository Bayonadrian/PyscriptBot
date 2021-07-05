from telegram.ext.conversationhandler import ConversationHandler
from dom.document import document

docVar = document()

def doc(update, context):

    update.message.reply_text('''/concept -> Para ver la funcion del objeto "document"
/element -> Para ver la propiedad "activeElement"'''
    )

    return 'doc'

def concept(update, context):

    update.message.reply_text(docVar.concept())

def element(update, context):

    update.message.reply_text(docVar.element())