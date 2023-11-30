import Server
def menu() -> bool:
    print("1) Reproducir video")
    print("2) Salir")
    option = int(input("Selecciona opción: "))
    if(option == 1):
        s = Server.Servidor()
        videos = s.fetch_videos()
        print("Videos:")
        for vid in videos:
            print(f"- {vid}")
        vid = int(input("¿Qué video deseas reproducir?"))
        
        
    elif(option == 2):
        print("Cerrando aplicación")
        return False
    else:
        print("Opción inválida")
    return True
    
