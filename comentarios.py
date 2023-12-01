import json
import cache as Cache

class Comentarios:

    def agregar_comentario(self, autor, contenido, comments):
        comments[autor] = contenido
        
    def obtener_comentarios(self, comments):
        print(comments)