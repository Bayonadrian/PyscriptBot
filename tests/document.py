import unittest
from dom.document import document

class Document_test(unittest.TestCase):

    def setUp(self) -> None:
        
        self.document = document()

    def test_concept(self):

        self.assertEqual('El objeto "document" hace referencia a cualquier documento HTML que carga el navegador, de este modo mediante este objeto se pueden acceder a los elementos HTML', self.document.concept())
        self.assertEqual('"activeElement", obtiene el elemento HTML enfocado', self.document.element())