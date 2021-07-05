from enum import Enum

class documentEx(Enum):

    element = 'Si uno enfoca, o hace click en un elemento HTML "form", entonces este retorna "form"'

class document:

    def concept(self):

        return 'El objeto "document" hace referencia a cualquier documento HTML que carga el navegador, de este modo mediante este objeto se pueden acceder a los elementos HTML'

    def element(self):

        return '"document.activeElement", obtiene el elemento HTML enfocado. Ej {}'.format(documentEx.element.value)