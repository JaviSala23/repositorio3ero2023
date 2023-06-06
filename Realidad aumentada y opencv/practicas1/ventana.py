import tkinter as tk
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self, window, video_source=0):
        self.window = window
        self.window.title("Aplicación de ejemplo")
        self.imagen= cv2.imread('foto.jpeg')
        shape=self.imagen.shape[:2]
   
        # Crear un elemento Canvas en la ventana
        self.canvas = tk.Canvas(window, width=shape[1], height=shape[0])
        self.canvas.pack()

        # Capturar video de la cámara
        #self.cap = cv2.VideoCapture(video_source)
        self.imagen= cv2.imread('foto.jpeg')
        self.update()

    def update(self):
        # Capturar un frame del video
        '''
        ret, frame = self.cap.read()

        if ret:
            # Convertir el frame de BGR a RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Crear una imagen PIL a partir del frame
            image = Image.fromarray(frame)

            # Convertir la imagen PIL a un objeto Tkinter PhotoImage
            self.photo = ImageTk.PhotoImage(image=image)

            # Actualizar el Canvas con la nueva imagen
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        '''
        # Crear una imagen PIL a partir del frame
        image = Image.fromarray(self.imagen)

        # Convertir la imagen PIL a un objeto Tkinter PhotoImage
        self.photo = ImageTk.PhotoImage(image=image)

        # Actualizar el Canvas con la nueva imagen
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        # Llamar a esta misma función recursivamente después de 15 milisegundos
        self.window.after(15, self.update)

# Crear la ventana y la aplicación
window = tk.Tk()
app = App(window)

# Iniciar el bucle principal de la aplicación
window.mainloop()





