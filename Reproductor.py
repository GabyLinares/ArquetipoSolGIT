import os
import time
import cache as Cache
import comentarios as Comentarios

class Reproductor:
    video = "#" # Arbitrario
    liked = False

    likes = None
    comments = None
    views = None
    space = None
    url = None

    cache = None

    def __init__(self, cache: Cache.GestorCache, videoURL: int):
        self.url = videoURL
        self.cache = cache
        self.play()
    
    def like(self):
        self.update(liked = self.liked)
        self.liked = not self.liked

    def play(self):
        (self.space, self.likes, self.comments, self.views) = self.cache.recibir_video(self.url)
        os.system("clear")
        print(f"========= VIDEO {self.url} =======")
        print("     o     "+    f"Vistas: {self.views}")
        print("    -|-     "+   f"Likes: {self.likes} (+{int(self.liked)} <3)")
        print("     n     "+    f"Comentarios: {len(self.comments)}")
        print(f"\n[{self.video}]")
        print(f"[{self.space}]")
        print("¿Qué acción deseas realizar?")
        print("1) Seguir viendo (añade vista)")
        print("2) Dar/quitar like (...)")
        print("3) Ver comentarios (...)")
        print("0) Salir del video")
        opt = int(input("-> "))
        match opt:
            case 1:
                if(len(self.video) != len(self.space)):
                    self.video *= len(self.space)
                    self.views += 1
                    self.update()
                
                self.play()
            case 2:
                self.like()
                self.play()
            case 3:
                Comentarios.comments(self.comments)
                self.play()
            case 0:
                pass
            case _:
                print("OPCIÓN INVÁLIDA")
                time.sleep(1.5)
                self.play()

    def update(self, liked = None):
        if(liked is not None and liked):
            self.likes -= 1

        elif(liked is not None and not liked):
            self.likes += 1
        self.cache.send(self.likes,self.views,self.comments, self.url)