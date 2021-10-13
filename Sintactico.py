from Token import Token
from Registro import Registro

class Sintactico:
    total = ''
    preanalisis = Token.ERROR
    posicion = 0
    lista = []
    tamano_val_registros = 0
    contador_registros = 0
    valor_actual = 0
    entro_reg = False
    errorSintactico = False
    print_consola = ''
    valores = []
    registros = Registro(-1)

    def __init__(self, lista):
        self.errorSintactico = False
        self.lista = lista
        self.lista.append(Token('`', Token.ULTIMO, -1, -1, -1))
        self.posicion = 0
        self.preanalisis = self.lista[self.posicion].tipo
        self.Inicio()

    def Match(self, tipo):
        if self.preanalisis != tipo:
            print(self.lista[self.posicion].lexema_valido, "--> Sintactico", " -- Se esperaba "+str(tipo))
            self.errorSintactico = True
            
        if self.preanalisis != Token.ULTIMO:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].tipo
        
        if self.preanalisis == Token.ULTIMO:
            print('Se ha finalizado el analisis sintactico')
            #print(self.registros.valores[0].args[0], self.registros.valores[0].indice) #['1', '"Barbacoa"', '10.50', '20.00', '6'] 0
            print(self.registros.valores[0].args[0][0], self.registros.valores[0].indice)
            print(self.registros.valores[1].args[0][0], self.registros.valores[1].indice)
            #print(len(self.registros.valores[1].args[0]), 'len')

    def Inicio(self):
        print('Inicio del analisis Sintáctico')
        if Token.CLAVES == self.preanalisis:
            self.Claves()
            self.Repetir()
        elif Token.REGISTROS == self.preanalisis:
            self.Registros()
            self.Repetir()
        elif Token.COMENTARIO_LINEA == self.preanalisis:
            self.Comentario()
            self.Repetir()    
        elif Token.COMENTARIO_MULTILINEA == self.preanalisis:
            self.Comentario_Multilinea()
            self.Repetir()     
        elif Token.IMPRIMIR == self.preanalisis:
            self.Imprimir()
            self.Repetir()
        elif Token.IMPRIMIRLN == self.preanalisis:
            self.ImprimirLn()
            self.Repetir()
        elif Token.CONTEO == self.preanalisis:
            self.Conteo()
            self.Repetir()
        elif Token.PROMEDIO == self.preanalisis:
            self.Promedio()
            self.Repetir()
        elif Token.CONTARSI == self.preanalisis:
            self.ContarSi()
            self.Repetir()
        elif Token.DATOS == self.preanalisis:
            self.Datos()
            self.Repetir()
        elif Token.SUMAR == self.preanalisis:
            self.Sumar()
            self.Repetir()
        elif Token.MAX == self.preanalisis:
            self.Max()
            self.Repetir()
        elif Token.MIN == self.preanalisis:
            self.Min()
            self.Repetir()
        elif Token.EXPORTARREPORTE == self.preanalisis:
            self.Exportar_Reporte()
            self.Repetir()
            
    def Claves(self):
        self.Match(Token.CLAVES)
        self.Match(Token.IGUAL)
        self.Match(Token.CORCHETE_IZQUIERDO)
        self.Cuerpo_Claves()
        self.Match(Token.CORCHETE_DERECHO)

    def Cuerpo_Claves(self):
        if Token.CADENA == self.preanalisis:
            self.Match(Token.CADENA)
        if Token.COMA == self.preanalisis:
            self.Match(Token.COMA)
            self.Cuerpo_Claves()
   
    def Registros(self):
        self.Match(Token.REGISTROS)
        self.Match(Token.IGUAL)
        self.Match(Token.CORCHETE_IZQUIERDO)
        self.Bloque_Registros()
        self.Match(Token.CORCHETE_DERECHO)
        
    def Bloque_Registros(self):
        if Token.LLAVE_IZQUIERDA == self.preanalisis:
            self.Cuerpo_Registros()
            self.Bloque_Registros()
    
    def Cuerpo_Registros(self):
        self.Match(Token.LLAVE_IZQUIERDA)
        self.valor_registro()
        self.Match(Token.LLAVE_DERECHA)
        self.guardar_registro()
    
    def guardar_registro(self):
        if not self.entro_reg:
            self.tamano_val_registros = len(self.valores)
            self.entro_reg = True
        values = self.valores[self.valor_actual:self.valor_actual + self.tamano_val_registros]
        self.registros.agregar_registro(self.contador_registros, values)
        self.contador_registros += 1
        self.valor_actual += self.tamano_val_registros
              
    def valor_registro(self):
        if Token.NUMERO == self.preanalisis:
            nuevo = self.lista[self.posicion].lexema_valido
            self.valores.append(nuevo)
            self.Match(Token.NUMERO)
        elif Token.CADENA == self.preanalisis:
            nuevo = self.lista[self.posicion].lexema_valido
            self.valores.append(nuevo)
            self.Match(Token.CADENA)    
        elif Token.DECIMAL == self.preanalisis:
            nuevo = self.lista[self.posicion].lexema_valido
            self.valores.append(nuevo)
            self.Match(Token.DECIMAL)
        if Token.COMA == self.preanalisis:
            self.Match(Token.COMA)
            self.valor_registro()
    
    def Comentario(self):
        self.Match(Token.COMENTARIO_LINEA)
    
    def Comentario_Multilinea(self):
        self.Match(Token.COMENTARIO_MULTILINEA)
        
    def Imprimir(self):
        self.Match(Token.IMPRIMIR)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.print_consola += self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA) 
    
    def ImprimirLn(self):
        self.Match(Token.IMPRIMIRLN)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.print_consola += self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA) 
        
    def Conteo(self):
        self.Match(Token.CONTEO)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA)    
    
    def Promedio(self):
        self.Match(Token.PROMEDIO)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA) 
        
    def ContarSi(self):
        self.Match(Token.CONTARSI)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.CADENA)
        self.Match(Token.COMA)     
        self.Match(Token.NUMERO)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)  
    
    def Datos(self):
        self.Match(Token.DATOS)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)               
    
    def Sumar(self):
        self.Match(Token.SUMAR)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)  
    
    def Max(self):
        self.Match(Token.MAX)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)  
        
    def Min(self):
        self.Match(Token.MIN)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)      
        
    def Exportar_Reporte(self):
        self.Match(Token.EXPORTARREPORTE)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)      
    
    def Repetir(self):
        if Token.CLAVES == self.preanalisis:
            self.Claves()
            self.Repetir()
        elif Token.REGISTROS == self.preanalisis:
            self.Registros()
            self.Repetir()
        elif Token.COMENTARIO_LINEA == self.preanalisis:
            self.Comentario()
            self.Repetir()    
        elif Token.COMENTARIO_MULTILINEA == self.preanalisis:
            self.Comentario_Multilinea()
            self.Repetir()     
        elif Token.IMPRIMIR == self.preanalisis:
            self.Imprimir()
            self.Repetir()
        elif Token.IMPRIMIRLN == self.preanalisis:
            self.ImprimirLn()
            self.Repetir()
        elif Token.CONTEO == self.preanalisis:
            self.Conteo()
            self.Repetir()
        elif Token.PROMEDIO == self.preanalisis:
            self.Promedio()
            self.Repetir()
        elif Token.CONTARSI == self.preanalisis:
            self.ContarSi()
            self.Repetir()
        elif Token.DATOS == self.preanalisis:
            self.Datos()
            self.Repetir()
        elif Token.SUMAR == self.preanalisis:
            self.Sumar()
            self.Repetir()
        elif Token.MAX == self.preanalisis:
            self.Max()
            self.Repetir()
        elif Token.MIN == self.preanalisis:
            self.Min()
            self.Repetir()
        elif Token.EXPORTARREPORTE == self.preanalisis:
            self.Exportar_Reporte()
            self.Repetir()