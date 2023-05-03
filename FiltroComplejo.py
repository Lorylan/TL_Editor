from Filtro import *

class FiltroComplejo(Filtro):
    def __init__(self, key, value) -> None:
        super().__init__()
        f=0
        if(key == "-CONTRASTE-"):
            f = (259 * (value + 255)) / (255 * (259 - value));
        dict_matriz = { "-BRILLO-" : [0,0,1,0,1,0,1,0,0,value,value,value],
                        "-AJ_ROJO-" : [0,0,1,0,1,0,1,0, 0,0,0,value],
                        "-AJ_VERDE-": [0,0,1,0,1,0,1,0, 0,0,value,0],
                        "-AJ_AZUL-":  [0,0,1,0,1,0,1,0, 0,value,0,0],  
                        "-CONTRASTE-": [f, 0, 0, 0, f, 0, 0, 0, f, 128*(1-f), 128*(1-f), 128*(1-f)],   
        }
        self.matriz = dict_matriz[key]