""" 
Herencia múltiple: Es un concepto en el que una clase puede heredar atributos y métodos de más de una clase.

"""

class Video:                                                                                        # Clase Video          
    def __init__(self, titulo_video, duracion, categoria):                                          # Constructor de la clase
        self.titulo_video = titulo_video                                                            # Definir tributo de la clase
        self.duracion = duracion
        self.categoria = categoria
    
    def mirar_video(self):                                                                         # Método para ver un video       
        print(f"Estás viendo el video {self.titulo_video}, con una duración de {self.duracion}")
    
    def detener_video(self):                                                                       # Método para detener un video
        print(f"Has detenido el video {self.categoria}")

class Audio:                                                                                       # Clase Audio   
    def __init__(self, titulo_audio, nombre_artista):
        self.titulo_audio = titulo_audio
        self.nombre_artista = nombre_artista
    
    def escuchar_audio(self):
        print(f"Estás escuchando la canción {self.titulo_audio}, del artista {self.nombre_artista}")
    
    def detener_audio(self):
        print(f"Has detenido la canción")

class Media(Video, Audio):                                                                         # Clase Media que hereda de Video y Audio      
    def __init__(self, titulo_video, titulo_audio, categoria, duracion, nombre_artista):
        Video.__init__(self, titulo_video, duracion, categoria)                                    # Llamar al constructor de la clase Video
        Audio.__init__(self, titulo_audio, nombre_artista)                                         # Llamar al constructor de la clase Video


                                                                                                   # Casos de uso: instanciar la clase y llamar a los métodos
reproductor = Media("Titulo Cualquiera", "Titulo Cualquiera 2 ","Serie", 50, "Artista desconocido")
""" 
reproductor.mirar_video()
reproductor.detener_video()
reproductor.escuchar_audio()
reproductor.detener_audio() 

"""