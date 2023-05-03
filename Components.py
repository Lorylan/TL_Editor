import PySimpleGUI as sg
import numpy as np

class Components(object):    
    def __text (self, text):
        return sg.Text(text)
    
    def __fileBrowser(self, button_text, file_types):
        return sg.FileBrowse(button_text, file_types=([(file_types)]))
    
    def __in(self, enable_events, key):
        return sg.In(enable_events=enable_events, key=key)
    
    def __image(self, key, width, height):
        return sg.Image(key=key, size=(width,height))
    
    def __button(self, button_name, key):
        return sg.Button(button_name, key=key)
    
    def __combo(self,values,key, default_value):
        return sg.Combo(values, key=key,enable_events=True, disabled=True, readonly=True, default_value=default_value)
    
    def __frame(self, title, layout,  width, height):
        return sg.Frame(title, [layout], size=(width, height))
    
    def __generateTextCombo(self,dictionary):
        elements = []
        for value in dictionary.values():
            elements.append(self.__text(value['text_value']))
            elements.append(self.__combo(value["values"],value['combo_key'], value['default_value']))
        return elements
    
    def __generateButtons(self, dictionary):
        elements = []
        for value in dictionary.values():
            elements.append(self.__button(value['button_name'] , value['key']))
        return elements
        
    def __getLayoutObtenerImagen(self):
        return[[self.__text("Editor de imagenes")],
               [self.__fileBrowser("Examinar",["PNG (*.png)","*.png"]),self.__in(True,'-SELECCIONO_IMAGEN-')],
               [self.__image('-IMAGEN-',600,400)]]
        
    def __getLayoutBotonesEdicion(self):
        dictionary = { "escala grises" : {'button_name': "Escala de grises" , 'key':  "-ESCALA_DE_GRISES-"} ,
                       "sepia" : {'button_name': "Sepia" , 'key':  "-SEPIA-"},
                      "voltear v" : {'button_name': "Voltear vertical" , 'key':  "-VOLTEAR_VERTICAL-"},
                      "voltear h" : {'button_name': "Voltear horizontal" , 'key':  "-VOLTEAR_HORIZONTAL-"},
                      "invertir" : {'button_name': "Invertir", 'key':"-INVERTIR-"}}
        return [self.__generateButtons({ "resetear" : {'button_name': "Resetear" , 'key' : "-RESETEAR-"}}) , self.__generateButtons(dictionary)]
        
    def __getLayoutBrilloColor(self):
        values_brillo = np.arange(-150,151,1).tolist()
        values_contraste = np.arange(-100,101,1).tolist()
        values_gamma = (np.arange(1,101)/ 10.0).tolist()
        dict_brillo = { "brillo": {'text_value': "Brillo", 'combo_key' : "-BRILLO-", 'values': values_brillo, 'default_value': 0}}
        dict_contraste = {"contraste": {'text_value': "Contraste" , 'combo_key' : "-CONTRASTE-", 'values': values_contraste, 'default_value': 0}}
        dict_gamma = {"correccion gamma" : {'text_value': "Correccion Gamma" , 'combo_key': "-GAMMA-", 'values': values_gamma, 'default_value':1.0}}
        return [self.__generateTextCombo(dict_brillo), self.__generateTextCombo(dict_contraste), self.__generateTextCombo(dict_gamma)]
        
    
    def __getLayoutCanales(self):
        values_aj = np.arange(-100, 101,1).tolist()
        dict_aj_rojo = { "ajuste rojo" : {'text_value' : "Ajuste del color rojo" , 'combo_key': "-AJ_ROJO-", 'values': values_aj, 'default_value': 0}}
        dict_aj_verde = {"ajuste verde" : {'text_value' : "Ajuste del color verde" , 'combo_key': "-AJ_VERDE-", 'values': values_aj, 'default_value': 0}}
        dict_aj_azul = {"ajuste azul" : {'text_value' : "Ajuste del color azul" , 'combo_key': "-AJ_AZUL-", 'values': values_aj, 'default_value': 0}}
        return [self.__generateTextCombo(dict_aj_rojo), self.__generateTextCombo(dict_aj_verde), self.__generateTextCombo(dict_aj_azul)]
        
    
    def __getLayoutEscalaresMover(self):
        values_escalar = (np.arange(1,101)/ 10.0).tolist()
        values_mover = np.arange(-100,101,1).tolist()
        dict_escalar_h = {"escalar h" : {'text_value' : "Escalar Horizontalmente" , 'combo_key': "-ESCALAR_H-", 'values': values_escalar, 'default_value': 1.00}}
        dict_escalar_v = {"escalar v" : {'text_value' : "Escalar Verticalmente" , 'combo_key' : "-ESCALAR_V-", 'values': values_escalar, 'default_value': 1.00}}
        dict_mover_h = {"mover h": {'text_value': "Mover Horizontalmente", 'combo_key' : "-MOVER_H-", 'values': values_mover, 'default_value': 0}}
        dict_mover_v = {"mover v" : {'text_value': "Mover Verticalmente", 'combo_key' : "-MOVER_V-", 'values': values_mover, 'default_value': 0}}
        
        return [self.__generateTextCombo(dict_escalar_h), self.__generateTextCombo(dict_escalar_v), self.__generateTextCombo(dict_mover_h), self.__generateTextCombo(dict_mover_v)]
        

    
    def __getLayoutEdicion(self):
        layout_botones_edicion = self.__getLayoutBotonesEdicion()
        layout_brillo_color = [sg.Column(self.__getLayoutBrilloColor())]
        layout_canales = [sg.Column(self.__getLayoutCanales())]
        layout_escalares_mover =[sg.Column(self.__getLayoutEscalaresMover())]
        
        
        dictionary= { "brillo_color" : {'title': "Brillo y Color",'layout': layout_brillo_color ,  'width': 300, 'height':150},
                                 "canales" : {'title': "Canales",'layout': layout_canales ,'width': 300, 'height':150},
                                 "escalares_mover": {'title': "Escalares y Mover", 'layout': layout_escalares_mover,'width': 300, 'height':150}
                                }
        
        frames = []
        
        for value in dictionary.values():
            frames.append(self.__frame(value['title'],value['layout'], value['width'], value['height']))
        
        return [[layout_botones_edicion], 
                [frames]] 
    
    def getComponents(self):
        return [self.__getLayoutObtenerImagen(), self.__getLayoutEdicion()]