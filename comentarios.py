class Comentarios:
    def __init__(self, c):
        # Simulación de la base de datos de comentarios
        self.comentarios = c

    def agregar_comentario(self, video, autor, contenido):
        if video not in self.comentarios: 
            self.comentarios[video] = []  

        comentario = {
            'autor': autor,
            'contenido': contenido
        }

        self.comentarios[video].append(comentario)

    def obtener_comentarios(self, video):
        return self.comentarios.get(video, [])