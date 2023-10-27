class Comentarios:
    def __init__(self):
        # Simulación de la base de datos de comentarios
        self.base_de_datos = {}

    def agregar_comentario(self, video, autor, contenido):
        # Mockup de función para añadir un comentario a la 'base de datos'
        if video not in self.base_de_datos:
            self.base_de_datos[video] = []

        comentario = {
            'autor': autor,
            'contenido': contenido
        }

        self.base_de_datos[video].append(comentario)

    def obtener_comentarios(self, video):
        # Obtener comentarios de un video seleccionado
        pass