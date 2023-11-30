import json

class Servidor:
    __active = False
    def __init__(self):
        f = open("Proyecto_reproduccion_videos/database.json")
        self.__active = True
        self.__videos = json.load(f)
        f.close()
        
    
    def fetch_videos(self):
        if self.__active:
            v = []
            for i in self.__videos:
                v.append(i)
            return v
        else:
            return None