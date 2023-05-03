import cv2
import numpy as np
import PySimpleGUI as sg


class Filtro(): 
    @property
    def matriz(self):
        return self.__matriz
    
    @matriz.setter
    def matriz(self, matriz):
        self.__matriz = matriz
    
    def aplicarFiltro(self,imagen,ancho,alto):
        matriz =  self.matriz
        try:
            for x in range(0,alto):
                for y in range(0,ancho):
                    b = imagen[x][y][0]
                    g = imagen[x][y][1]
                    r = imagen[x][y][2]
                    
                    new_b = matriz[0]*r + matriz[3]*g + matriz[6]*b + matriz[9];
                    new_g = matriz[1]*r + matriz[4]*g + matriz[7]*b + matriz[10];
                    new_r = matriz[2]*r + matriz[5]*g + matriz[8]*b + matriz[11];
                
                    #Por si se pasa del rango (0-255)
                    imagen[x][y][0] = 255 if(new_b > 255) else (0 if (new_b < 0) else new_b)
                    imagen[x][y][1] = 255 if(new_g > 255) else (0 if (new_g < 0) else new_g)
                    imagen[x][y][2] = 255 if(new_r > 255) else (0 if (new_r < 0) else new_r) 
            return cv2.imencode(".png", imagen)[1].tobytes(),imagen
        except :
            sg.popup("Ocurrio un error al aplicar el filtro",title="Error")
            print("Ocurrio un error al aplicar el filtro")
            
    
    def aplicarVoltear(self, imagen, ancho, alto):
        matriz = self.matriz
        try:
            imagen_volteada = np.zeros((alto,ancho,3), dtype=np.uint8)
            for x in range(0,alto):
                for y in range(0,ancho):
                    new_x = matriz[0]*x + matriz[1]*y 
                    new_y = matriz[2]*x + matriz[3]*y
                    imagen_volteada[new_x,new_y]= imagen[x,y]
            imagen = np.copy(imagen_volteada)
            return cv2.imencode(".png", imagen)[1].tobytes(), imagen
        except:
            sg.popup("Ocurrio un error al aplicar el volteo de la imagen",title="Error")
            print("Ocurrio un error al aplicar el volteo de la imagen")
               
    def aplicarTransformaciones(self, imagen, ancho, alto, evento):
        key_interpolacion = ["-ESCALAR_V-","-ESCALAR_H-"]
        aplicar_interpolacion = True if evento in key_interpolacion else False
        matriz = self.matriz
        try:
            imagen_transformada = np.zeros((alto,ancho,3), dtype=np.uint8)
            for x in range(alto):
                for y in range(ancho):
                    new_x = int(matriz[0]*x + matriz[1]*y + matriz[2])
                    new_y = int(matriz[3]*x + matriz[4]*y + matriz[5])
                    #Chequeo que no me pase del tamaño de la imagen
                    if( new_x >= 0 and new_y >=0 and new_x < alto and new_y < ancho): 
                        imagen_transformada[new_x, new_y] = imagen[x,y]
                        #Aplicamos interpolacion por el vecino mas cercano
                        if(aplicar_interpolacion):
                            if (new_x+1 >=0 and new_x+1 < alto):
                                imagen_transformada[new_x +1, new_y] = imagen[x,y]
                            if (new_y+1 >=0 and new_y+1 < ancho):
                                imagen_transformada[new_x, new_y+1] = imagen[x,y]
                            if((new_x+1 >=0 and new_x+1 < alto)and (new_y+1 >=0 and new_y+1 < ancho)):
                                imagen_transformada[new_x+1, new_y+1] = imagen[x,y]
            imagen = np.copy(imagen_transformada)
            return cv2.imencode(".png", imagen)[1].tobytes(), imagen
        except: 
            sg.popup("Ocurrio un error al aplicar la trasformacion a la imagen",title="Error")
            print("Ocurrio un error al aplicar la trasformacion a la imagen")

            
    def aplicarGamma(self, imagen, alto,ancho, value):
        try:
            for x in range(0,alto):
                for y in range(0,ancho):
                    b = imagen[x][y][0]
                    g = imagen[x][y][1]
                    r = imagen[x][y][2]
                    
                    new_b = 255 * pow(b / 255, 1/value);
                    new_g = 255 * pow(g / 255, 1/value);
                    new_r = 255 * pow(r / 255, 1/value);
                
                    #Por si se pasa del rango (0-255)
                    imagen[x][y][0] = 255 if(new_b > 255) else (0 if (new_b < 0) else new_b)
                    imagen[x][y][1] = 255 if(new_g > 255) else (0 if (new_g < 0) else new_g)
                    imagen[x][y][2] = 255 if(new_r > 255) else (0 if (new_r < 0) else new_r) 
            return cv2.imencode(".png", imagen)[1].tobytes(),imagen
        except:
            sg.popup("Ocurrio un error al aplicar la correccion de gamma a la imagen",title="Error")
            print("Ocurrio un error al aplicar la correccion de gamma a la imagen")
        
        
        