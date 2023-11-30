import os
import Reproductor
import cache as Cache
def menu(c: Cache.GestorCache) -> bool:
    print("\n")
    print("1) Reproducir video")
    print("2) Salir")
    option = int(input("\nSelecciona opción: "))
    os.system("clear")
    if(option == 1):
        videos = c.recibir_lista_videos()
        print("\nVideos:")
        for vid in videos:
            print(f"- {vid}")
        while True:
            vid = int(input("\n¿Qué video deseas reproducir?\n(Presiona 0 para salir)\n -> "))
            if(0 < vid and vid <= len(videos)):
                break
            elif(vid == 0):
                return True
            else:
                print("OPCIÓN INVÁLIDA.")
        Reproductor.Reproductor(cache = c, videoURL = vid)
        

        
        
    elif(option == 2):
        print("\nCerrando aplicación")
        return False
    else:
        print("\nOpción inválida")
    return True
    

