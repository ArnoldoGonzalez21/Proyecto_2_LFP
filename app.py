from tkinter import *
import tkinter
from tkinter import Frame, ttk, filedialog
from Analizador import Analizador
from Sintactico import Sintactico

WIDTH = 800
HEIGHT = 550

class Interfaz():
    nombre = ''
    lexico = Analizador()
    ventana = tkinter.Tk()     
    
    def __init__(self):
        self.configuracion_ventana()        
        combo_imagenes = ttk.Combobox(self.ventana, font = ('Courier', 11), state = "readonly")
        self.crear_toolbar()
        self.crear_txt()
        self.ventana.mainloop()
        
    def configuracion_ventana(self):
        self.ventana.geometry(str(WIDTH)+"x"+str(HEIGHT))
        self.ventana.title('Lenguaje') 
    
    def crear_toolbar(self):
        toolbar = Frame(self.ventana, bg = 'white')         
        boton_abrir = tkinter.Button(toolbar, text = 'Abrir', command = self.leer_archivo, width = 10, height = 2)
        boton_analizar = tkinter.Button(toolbar, text = 'Analizar', command = self.analizar_archivo, width = 10, height = 2)
        boton_reportes = tkinter.Button(toolbar, text = 'Reportes', command = self.crear_reportes,  width = 10, height = 2)
        boton_salir = tkinter.Button(toolbar, text = 'Salir', command = lambda: exit(), width = 10, height = 2)
        
        label_titulo = tkinter.Label(toolbar, text = "Proyecto 2 - 201701548", font = ('Courier', 11), bg = 'white')
        
        label_titulo.pack(side = LEFT, padx = 3, pady = 2)
        boton_salir.pack(side = RIGHT, padx = 3, pady = 2)
        boton_reportes.pack(side = RIGHT, padx = 3, pady = 2) 
        boton_analizar.pack(side = RIGHT, padx = 3, pady = 2)
        boton_abrir.pack(side = RIGHT, padx = 3, pady = 2)
        toolbar.pack(side = TOP, fill = X)
    
    def crear_txt(self):
        self.txt_consola = tkinter.Text(self.ventana, height = 27, width = 35, font = ('Courier', 10), bg = 'white')
        self.txt_entrada = tkinter.Text(self.ventana, height = 27, width = 50, font = ('Courier', 10), bg = 'white')
        self.txt_entrada.place(x = 50, y = 75) 
        self.txt_consola.place(x = 485, y = 75) 
        self.txt_consola.insert(tkinter.INSERT, 'Hola')  
        
    def analizar_archivo(self):
        contenido_Text = self.txt_entrada.get("1.0", tkinter.END)
        self.lexico.analizador_estados(contenido_Text)
        #self.lexico.obtener_tokens()
        #self.lexico.guardar_imagen()        
        #self.configuracion_combo(combo_imagenes)
        #self.lexico.Imprimir()    
    
    def configuracion_combo(self, combo_imagenes):
        self.lexico.opciones_imagenes(combo_imagenes)
        combo_imagenes.place(x = 370, y = 30)
        
    def crear_reportes(self):
        sintactico = Sintactico(self.lexico.tokens)
        #self.lexico.obtener_tokens()
        #self.lexico.obtener_errores()
        #self.lexico.crear_reporte_token()
        #self.lexico.crear_reporte_errores()
        
    def leer_archivo(self):
        try:
            ruta = filedialog.askopenfilename(title = "Abrir un archivo")
            with open(ruta, 'rt', encoding = 'utf-8') as f:
                print('Archivo cargado con éxito')
                self.data = f.read()  
                self.txt_entrada.insert(tkinter.INSERT, self.data)      
        except OSError:
            print("<<< No se pudo leer el Archivo", ruta ,'>>>')
            return   
    
if __name__ == '__main__':
    Interfaz()