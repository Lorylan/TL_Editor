# Librerias #
import PySimpleGUI as sg
from Components import *
from FiltroComplejo import *
from FiltroSimple import *
from Transformar import *


def main ():
    key_filtro_simple= ["-ESCALA_DE_GRISES-","-SEPIA-","-INVERTIR-"]
    key_voltear = ["-VOLTEAR_VERTICAL-","-VOLTEAR_HORIZONTAL-"]
    key_filtro_complejo = ["-BRILLO-", "-AJ_ROJO-", "-AJ_VERDE-", "-AJ_AZUL-","-CONTRASTE-"]
    key_transform=["-ESCALAR_H-","-ESCALAR_V-","-MOVER_V-", "-MOVER_H-"]
    clave_componentes=['-BRILLO-',"-CONTRASTE-","-AJ_ROJO-","-AJ_VERDE-","-AJ_AZUL-","-MOVER_H-",
                    "-MOVER_V-","-GAMMA-","-ESCALAR_H-","-ESCALAR_V-"]
    
    window = sg.Window('Editor de imagenes con  TL', Components().getComponents(), resizable=True)
    
    imagen = []
    ancho = 600
    alto = 400
    path_imagen= ""

    #Event Loop para procesar "eventos" y obtener los "valores" de las entradas
    while True:
        evento, valores = window.read()
        
        if evento == sg.WIN_CLOSED or evento == 'Cancel': 
            break
        
        elif evento == "-SELECCIONO_IMAGEN-":
            try:
                path_imagen = valores["-SELECCIONO_IMAGEN-"]
                imagen = cv2.imread(path_imagen)
                imagen = cv2.resize(imagen,[ancho,alto])
                imgbyte = cv2.imencode(".png", imagen)[1].tobytes()
                window["-IMAGEN-"].update(data=imgbyte)
                for key in clave_componentes:
                    window[key].update(disabled=False)
            except:
                sg.popup("Ocurrio un error el intentar abrir la imagen.",title="Error")
          
        elif (path_imagen == ""):
            sg.popup("Primero seleccione una imagen antes de aplicar un filtro",title="Error")
              
        elif evento in key_filtro_simple:
            filtro_simple = FiltroSimple(evento)
            imgbyte, img = filtro_simple.aplicarFiltro(imagen,ancho,alto)
            window["-IMAGEN-"].update(data=imgbyte)
            imagen= img
        
        elif evento in key_voltear:
            filtro_simple = FiltroSimple(evento)
            imgbyte, img = filtro_simple.aplicarVoltear(imagen,ancho,alto)
            window["-IMAGEN-"].update(data=imgbyte)
            imagen= img
            
        elif evento in key_filtro_complejo:
            filtro_complejo = FiltroComplejo(evento, valores[evento])
            imgbyte,img = filtro_complejo.aplicarFiltro(imagen, ancho,alto)
            window["-IMAGEN-"].update(data=imgbyte)
            imagen = img
        
        elif evento in key_transform:
            filtro = Transformar(evento, valores[evento],ancho,alto)
            imgbyte,img = filtro.aplicarTransformaciones(imagen,ancho,alto,evento)
            window["-IMAGEN-"].update(data=imgbyte)
            imagen = img
            
        elif evento == "-GAMMA-":
            filtro = Filtro()
            imgbyte,img = filtro.aplicarGamma(imagen,alto,ancho, valores[evento])
            window["-IMAGEN-"].update(data=imgbyte)
            imagen = img
    
        elif evento == "-RESETEAR-":
            dict_zero_defaults = {"-BRILLO-", "-CONTRASTE-", "-AJ_ROJO-", "-AJ_VERDE-", "-AJ_AZUL-", "-MOVER_V-", "-MOVER_H-"}
            dict_one_defaults = {"-GAMMA-","-ESCALAR_H-", "-ESCALAR_V-"}
            imagen = cv2.imread(path_imagen)
            imagen = cv2.resize(imagen,[ancho,alto])
            imgbyte = cv2.imencode(".png", imagen)[1].tobytes()
            window["-IMAGEN-"].update(data=imgbyte)
            for key in dict_zero_defaults:
                window[key].update(value=0)
            for key in dict_one_defaults:
                window[key].update(value=1.0)
        
    window.close()

if __name__ == "__main__":
    main()
    
