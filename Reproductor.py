import os
import time
import cache as Cache
from comentarios import Comentarios
import random

class Reproductor:
    video = "#" # Arbitrario
    liked = False

    likes = None
    comments = None
    comentarios_instance = Comentarios()
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
        print("3) Comentarios (...)")
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
                print("")
                self.handle_comments()
                
            case 0:
                pass
            case _:
                print("OPCIÓN INVÁLIDA")
                time.sleep(1.5)
                self.play()

    def handle_comments(self):
        print("")
        print("¿Qué acción deseas realizar?")
        print("1) Ver comentarios")
        print("2) Añadir un comentario")
        comments_opt = int(input("-> "))

        if comments_opt == 1:
            self.show_comments()
        elif comments_opt == 2:
            print("Ingrese su comentario por favor: ")
            comentario = input("-> ")
            self.comentarios_instance.agregar_comentario(f"user{random.randint(100, 999)}", comentario, self.comments)
            self.cache.send(self.likes,self.views,self.comments, self.url)
            # print(self.comments)
        else:
            print("OPCIÓN INVÁLIDA")
            time.sleep(1.5)
            self.play()

    def show_comments(self):
        self.comentarios_instance.obtener_comentarios(self.comments)

    def update(self, liked = None):
        if(liked is not None and liked):
            self.likes -= 1

        elif(liked is not None and not liked):
            self.likes += 1
        self.cache.send(self.likes,self.views,self.comments, self.url)