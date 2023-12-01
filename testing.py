import json
import comentarios, Server, analista, cache, Reproductor
import pytest
import unittest
from comentarios import Comentarios
from Server import Servidor
from analista import Analista
from analista import Servidor as srvr
from cache import GestorCache
from Reproductor import Reproductor
from unittest.mock import MagicMock
from unittest.mock import patch



class Testeo(unittest.TestCase):

    def setUp(self):
        self.comments = {}
        self.comentarios_obj = Comentarios()

        self.servidor = Servidor()
        self.srvr = srvr()
        self.analista = Analista(self.servidor)

        self.GestorCache = cache.GestorCache()
        self.videoURL = 1
        self.reproductor = Reproductor(self.GestorCache, self.videoURL)

    def test_agregar_comentario(self):
        #testearemos que los comentarios se guarden correctamente
        self.comentarios_obj.agregar_comentario("Juan", "Este es un comentario", self.comments)
        self.assertEqual(self.comments["Juan"], "Este es un comentario")

    def test_obtener_comentarios(self):
        #testeamos que al ver los comentarios sean los correctos
        self.comentarios_obj.agregar_comentario("Juan", "Este es un comentario", self.comments)
        self.comentarios_obj.agregar_comentario("Pedro", "Este es otro comentario", self.comments)
        self.comentarios_obj.obtener_comentarios(self.comments)
        self.assertEqual(self.comments, {"Juan": "Este es un comentario", "Pedro": "Este es otro comentario"})

    def test_calcular_porcentaje_permanencia_sin_visualizaciones(self):
        #si nadie lo ha visto deberia ser sero
        video = "video"
        porcentaje = self.analista.calcular_porcentaje_permanencia(video)
        self.assertEqual(porcentaje, 0)

    def test_calcular_porcentaje_permanencia_con_visualizaciones(self):
        #simulamos que vemos la mitad en un video de 60 segundos
        self.servidor.registrar_visualizacion("video", 30)
        #que el video si dure 60 segundos
        self.servidor.obtener_duracion_total.return_value = 60

        porcentaje = self.analista.calcular_porcentaje_permanencia("video")
        #nos aseguramos que sea la mitad
        self.assertEqual(porcentaje, 50)

    def test_calcular_porcentaje_permanencia_con_duraciones_cero(self):
        #registranis 30 segundos vistos
        self.servidor.registrar_visualizacion("video", 30)
        #obtebenis la duracion del video
        self.servidor.obtener_duracion_total.return_value = 0

        porcentaje = self.analista.calcular_porcentaje_permanencia("video")
        #que pasa si dura 0
        self.assertEqual(porcentaje, 0)


if __name__ == "__main__":
    unittest.main()
