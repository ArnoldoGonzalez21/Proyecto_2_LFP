from tkinter import *
import tkinter
from tkinter import Frame, ttk, filedialog
from Analizador import Analizador
from Sintactico import Sintactico

WIDTH = 1025
HEIGHT = 550

class Interfaz():
    nombre = ''
    lexico = Analizador()
    ventana = tkinter.Tk()     
    
    def __init__(self):
        self.configuracion_ventana()    
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
        boton_reportes = tkinter.Button(toolbar, text = 'Reporte', command = self.crear_reportes,  width = 10, height = 2)
        boton_salir = tkinter.Button(toolbar, text = 'Salir', command = lambda: exit(), width = 10, height = 2)
        label_titulo = tkinter.Label(toolbar, text = "Proyecto 2 - 201701548", font = ('Courier', 11), bg = 'white')
        label_entrada = tkinter.Label(self.ventana, text = "Terminal de Entrada", font = ('Courier', 13))
        label_consola = tkinter.Label(self.ventana, text = "Consola", font = ('Courier', 13))
        
        label_titulo.pack(side = LEFT, padx = 3, pady = 2)
        boton_salir.pack(side = RIGHT, padx = 3, pady = 2)
        boton_reportes.pack(side = RIGHT, padx = 3, pady = 2) 
        self.configuracion_combo(toolbar)
        boton_analizar.pack(side = RIGHT, padx = 3, pady = 2)
        boton_abrir.pack(side = RIGHT, padx = 3, pady = 2)
        toolbar.pack(side = TOP, fill = X)
        
        label_entrada.place(x = 175, y = 65)
        label_consola.place(x = 725, y = 65)
    
    def crear_txt(self):
        self.txt_consola = tkinter.Text(self.ventana, height = 27.50, width = 58, font = ('Courier', 9), bg = 'white', state = 'disabled')
        self.txt_entrada = tkinter.Text(self.ventana, height = 26, width = 63, font = ('Courier', 10), bg = 'white')
        self.txt_entrada.place(x = 30, y = 100) 
        self.txt_consola.place(x = 565, y = 100) 
        
        scrollbar_entrada = ttk.Scrollbar(self.ventana, orient = "vertical", command = self.txt_entrada.yview)
        scrollbar_entrada.place(x = 538, y = 100, height = 420) 
        self.txt_entrada.configure(yscrollcommand = scrollbar_entrada.set)
        
        scrollbar_consola = ttk.Scrollbar(self.ventana, orient = "vertical", command = self.txt_consola.yview)
        scrollbar_consola.place(x = 975, y = 100, height = 420) 
        self.txt_consola.configure(yscrollcommand = scrollbar_consola.set)
        
    def analizar_archivo(self):
        self.txt_consola.configure(state = 'normal')
        self.txt_consola.delete('1.0', END)  
        contenido_Text = self.txt_entrada.get("1.0", tkinter.END)
        self.lexico.reiniciar_tokens()
        self.lexico.analizador_estados(contenido_Text)
        
        self.sintactico = Sintactico(tkinter, self.lexico.tokens, self.txt_consola)
        self.txt_consola.configure(state = 'disabled')
        self.lexico.obtener_tokens()      
        self.sintactico.reniciar()
    
    def configuracion_combo(self, toolbar):    
        self.combo_reportes = ttk.Combobox(toolbar, font = ('Courier', 9), width = 25,  state = "readonly")
        self.combo_reportes["values"] = ["Seleccione el Reporte", "Reporte Tokens", "Reporte Errores Léxicos", "Reporte Error Sintáctico"]
        self.combo_reportes.current(0)
        self.combo_reportes.pack(side = RIGHT, padx = 3, pady = 2) 
        
    def crear_reportes(self):
        indice = self.combo_reportes.current()
        if indice == 1:
            self.lexico.crear_reporte_token()
        elif indice == 2:
            self.lexico.crear_reporte_errores()
        elif indice == 3:
            self.sintactico.crear_reporte_errores_sintactico()
        
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