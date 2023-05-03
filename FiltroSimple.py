from Filtro import * 

class FiltroSimple(Filtro):
    
    def __init__(self,key) -> None:
        #Contructor para filtros simples
        super().__init__()
        dict_matriz = {"-ESCALA_DE_GRISES-" : [1/3,1/3,1/3,1/3,1/3,1/3,1/3,1/3,1/3,0,0,0],
                     "-SEPIA-" :[0.272, 0.349, 0.393, 0.534, 0.686, 0.769, 0.131, 0.168, 0.189,0,0,0],
                     "-INVERTIR-": [-1, 0, 0, 0, -1, 0, 0, 0, -1, 255, 255, 255],
                     "-VOLTEAR_VERTICAL-": [-1,0,0,1],
                     "-VOLTEAR_HORIZONTAL-":[1,0,0,-1]  
                    }
        self.matriz = dict_matriz[key]