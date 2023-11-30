import Server
class GestorCache:
    def __init__(self):
        self.video_cache:str = "#"
        self.lista_cache:list = []
        self.comentarios_cache:list = []
        self.server = Server.Servidor()
    
    def recibir_lista_videos(self):
        return self.server.fetch_video_list()

    def recibir_video(self, video):
        data = self.calcular_espacio_necesario(video)
        return (self.video_cache, data["likes"], data["comments"], data["views"])

    def calcular_espacio_necesario(self, video):
        self.eliminar_videos_antiguos()
        data = self.server.fetch_video(video)
        self.video_cache *= data["duration"]
        return data

    def eliminar_videos_antiguos(self):
        self.video_cache = "#"
    

    def send(self, likes,views,comments, url):
        self.server.send(likes,views,comments, url)
