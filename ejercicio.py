import turtle 
import os
import random
from PIL import Image, ImageTk 

contador = 0

#Funcion para obtener la ruta de los recursos 
def rescourse_path(relative_path):
    return os.path.join(os.path.abspath('.'),relative_path)

#Configurar la ventana
wn = turtle.Screen()
wn.title('Juego de Programacion')
wn.setup(width=600, height=600)
wn.bgcolor('white')
wn.tracer(0) #Desactiva el refresco automatico para animacion suave 

canvas = wn.getcanvas() #Obtrenemos el canvas de la ventana

#Funcion para crear una imagen en el canvas 
def crear_imagen(x, y, imagen_path):
    img = Image.open(imagen_path)
    tk_img = ImageTk.PhotoImage(img)
    image_id = canvas.create_image(x, y, image=tk_img)
    return{'id': image_id, 'img_ref': tk_img, 'x':x,'y': y}

#Crear personajes y objeto de llegada 
cuerpo = crear_imagen(125, -220, rescourse_path('bicicleta.jpg'))
cabeza = crear_imagen(120, -280, rescourse_path('player.jpg'))
comida = crear_imagen(-100, 80, rescourse_path('gasolina.png'))

#Funcion para mover una imagen
def mover(imagen, dx, dy):
    imagen['x'] += dx
    imagen['y'] += dy
    canvas.coords(imagen['id'], imagen['x'], imagen['y'])

#Controles para el personaje
def arriba():
    mover(cabeza, 0, -20)
    mover(cuerpo, 0, -20)

def abaj0():
    mover(cabeza, 0, 20)
    mover(cuerpo, 0, 20)

def izquierda():
    mover(cabeza, -20, 0)
    mover(cuerpo, -20, 0)

def derecha():
    mover(cabeza, 20, 0)
    mover(cuerpo, 20, 0)

#Configurar teclas
wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')

