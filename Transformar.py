from Filtro import *

class Transformar(Filtro):
    
    def __init__(self,key,value,ancho,alto) -> None:
        
        #Contructor para filtros simples
        super().__init__()
        dict_matriz = {  "-ESCALAR_V-" : [value,0,0,0,1,0,0,1],
                        "-ESCALAR_H-" : [1,0,0,0,value,0,0,0,1],
                        "-MOVER_H-" : [1,0,0,0,1,(value*ancho)/100,0,0,1],
                        "-MOVER_V-" : [1,0,(value*alto)/100,0,1,0,0,0,1],
                    }
        self.matriz = dict_matriz[key]