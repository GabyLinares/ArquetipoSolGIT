import json

class Servidor:
    __active = False
    __videos = None
    def __init__(self):
        f = open("C:/Users/Ángel/Documents/UR 2023-2/Dis y Arq Software/ArquetipoSolGIT/database.json")
        self.__videos = json.load(f)
        self.__active = True
        
    
    def fetch_video_list(self):
        if self.__active:
            v = []
            for i in self.__videos:
                v.append(i)
            return v
        else:
            return None
    
    def fetch_video(self, url: int):
        f = open("C:/Users/Ángel/Documents/UR 2023-2/Dis y Arq Software/ArquetipoSolGIT/database.json")
        self.__videos = json.load(f)

        if self.__active:
            return self.__videos[f"video{url}"]
        else:
            return None
    
    def send(self, likes,views,comments, url):
        if self.__active:
            self.__videos[f"video{url}"]["likes"] = likes
            self.__videos[f"video{url}"]["views"] = views
            self.__videos[f"video{url}"]["comments"] = comments
            with open('C:/Users/Ángel/Documents/UR 2023-2/Dis y Arq Software/ArquetipoSolGIT/database.json', 'w') as f:
                f.write(json.dumps(self.__videos))
        else:
            pass