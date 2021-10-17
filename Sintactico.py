from Token import Token
from Registro import Registro
from Clave import Clave
import webbrowser
from Arboles import Arboles
from os import makedirs

class Sintactico:
    
    arboles = Arboles()
    tipos = Token('',-1,-1,-1)
    preanalisis = Token.ERROR
    posicion = 0
    lista = []
    tamano_val_registros = 0
    contador_registros = 0
    valor_actual = 0
    indice_clave = 0
    entro_reg = False
    errorSintactico = False
    valores_registro = []
    valores_clave = []
    registros = Registro(-1)
    reporteHTML_registro = ''
    reporte_error_sintac = ''
    nombres_arboles = []

    def __init__(self, tkinter, lista, txt_consola):
        self.errorSintactico = False
        self.lista = lista
        self.tkinter = tkinter
        self.txt_consola = txt_consola
        self.lista.append(Token('`', Token.ULTIMO, -1, -1))
        self.posicion = 0
        self.preanalisis = self.lista[self.posicion].tipo
        self.Inicio()

    def Match(self, tipo):
        if self.preanalisis != tipo:
            font = '<font color=\"#000000\" face=\"Courier\">'
            print(self.lista[self.posicion].lexema_valido, "--> Sintactico", " -- Se esperaba "+str(self.tipo_token(tipo)))
            self.reporte_error_sintac += '<tr><td align=center>'+ font + self.lista[self.posicion].lexema_valido + ' --> Se esperaba --> ' + str(self.tipo_token(tipo))
            self.reporte_error_sintac += '</td><td align=center><font color=\"#155CFF\" face=\"Courier\">Error Sintáctico </td><td align=center>'+ font + str(self.lista[self.posicion].fila)
            self.reporte_error_sintac += '</td><td align=center>'+ font + str(self.lista[self.posicion].columna) + '</td></tr>'
            self.errorSintactico = True
            
        if self.preanalisis != Token.ULTIMO:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].tipo
        
        if self.preanalisis == Token.ULTIMO:
            print('Se ha finalizado el analisis sintactico')
    
    def tipo_token(self, tipo):
        nombre_Tk = self.tipos.get_tipo_token_sintactico(tipo)
        return nombre_Tk
    
    contenido_inicio = ''        
    contador_inicio = 1
    
    def Inicio(self):
        print('Inicio del analisis Sintáctico')
        if Token.CLAVES == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<CLAVES>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'       
            self.contador_inicio += 1
            self.Claves()
            self.Repetir()
        elif Token.REGISTROS == self.preanalisis:         
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REGISTROS>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'       
            self.contador_inicio += 1
            self.Registros()
            self.Repetir()
        elif Token.COMENTARIO_LINEA == self.preanalisis:      
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<COMENTARIO_LINEA>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'       
            self.contador_inicio += 1
            self.Comentario()
            self.Repetir()    
        elif Token.COMENTARIO_MULTILINEA == self.preanalisis:           
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<COMENTARIO_MULTILINEA>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'       
            self.contador_inicio += 1
            self.Comentario_Multilinea()
            self.Repetir()     
        elif Token.IMPRIMIR == self.preanalisis:           
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<IMPRIMIR>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'       
            self.contador_inicio += 1
            self.Imprimir()
            self.Repetir()
        elif Token.IMPRIMIRLN == self.preanalisis:     
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<IMPRIMIRLN>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'       
            self.contador_inicio += 1
            self.ImprimirLn()
            self.Repetir()
        elif Token.CONTEO == self.preanalisis:         
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<CONTEO>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'   
            self.contador_inicio += 1
            self.Conteo()
            self.Repetir()
        elif Token.PROMEDIO == self.preanalisis:       
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<PROMEDIO>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'    
            self.contador_inicio += 1
            self.Promedio()
            self.Repetir()
        elif Token.CONTARSI == self.preanalisis:           
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<CONTARSI>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n' 
            self.contador_inicio += 1
            self.ContarSi()
            self.Repetir()
        elif Token.DATOS == self.preanalisis:        
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<DATOS>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'    
            self.contador_inicio += 1
            self.Datos()
            self.Repetir()
        elif Token.SUMAR == self.preanalisis:           
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<SUMAR>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n' 
            self.contador_inicio += 1
            self.Sumar()
            self.Repetir()
        elif Token.MAX == self.preanalisis:         
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<MAX>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'  
            self.contador_inicio += 1
            self.Max()
            self.Repetir()
        elif Token.MIN == self.preanalisis:     
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<MIN>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'      
            self.contador_inicio += 1
            self.Min()
            self.Repetir()
        elif Token.EXPORTARREPORTE == self.preanalisis:         
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<EXPORTAR_REPORTE>"];\n'
            self.contenido_inicio += 'n0 -> n'+str(self.contador_inicio)+';\n'   
            self.contador_inicio += 1
            self.Exportar_Reporte()
            self.Repetir()
    
    def arbol_inicio(self):
        return self.contenido_inicio
    
    contenido_claves = ''        
    contador_claves = 4
           
    def Claves(self):
        self.contenido_claves = ''        
        self.contador_claves = 4
        self.Match(Token.CLAVES)
        self.Match(Token.IGUAL)
        self.Match(Token.CORCHETE_IZQUIERDO)
        self.Cuerpo_Claves()
        self.contenido_claves += 'n'+str(self.contador_claves)+'[label = "]"];\n'
        self.contenido_claves += 'raiz -> n'+str(self.contador_claves)+';'       
        self.Match(Token.CORCHETE_DERECHO)
        
        if not self.repetido('Arbol Claves'):
            self.nombres_arboles.append('Arbol Claves')

    def Cuerpo_Claves(self):
        if Token.CADENA == self.preanalisis:
            nombre = self.lista[self.posicion].lexema_valido
            nombre = nombre.replace('"','')
            nuevo = Clave(self.indice_clave, nombre)
            self.valores_clave.append(nuevo)
            self.indice_clave += 1
            
            self.contenido_claves += 'n'+str(self.contador_claves)+'[label = "<BLOQUE_CLAVES>"];\n'
            self.contenido_claves += 'n'+str(self.contador_claves)+' -> n'+str(self.contador_claves + 1)+';\n'
            self.contador_claves += 1
            self.contenido_claves += 'n'+str(self.contador_claves)+'[label = "'+nombre.replace('_',' ')+'"];\n'
            self.contador_claves += 1
            
            self.Match(Token.CADENA)
        if Token.COMA == self.preanalisis:
            self.contenido_claves += 'n'+str(self.contador_claves)+'[label = ","];\n'
            self.contenido_claves += 'n'+str(self.contador_claves - 2)+' -> n'+str(self.contador_claves)+';\n'
            self.contenido_claves += 'n'+str(self.contador_claves - 2)+' -> n'+str(self.contador_claves + 1)+';\n'
            self.contador_claves += 1
            self.Match(Token.COMA)
            self.Cuerpo_Claves()   
    
    def arbol_claves(self):
        contenido = '''
        \r\t\tn1[label = "Claves"];
        \r\t\tn2[label = "="];
        \r\t\tn3[label = "["];  
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;'''
        contenido += self.contenido_claves
        return contenido        
    
    contenido_registros = ''        
    contador_registros = 4
    
    def Registros(self):
        self.contenido_registros = ''        
        self.contador_registros = 4
        self.Match(Token.REGISTROS)
        self.Match(Token.IGUAL)
        self.Match(Token.CORCHETE_IZQUIERDO)
        self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "<BLOQUE_REGISTROS>"];\n'
        self.contador_registros += 1
        self.Bloque_Registros()
        self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "]"];\n'
        self.contenido_registros += 'raiz -> n'+str(self.contador_registros)+';\n'
        self.contador_registros += 1
        self.Match(Token.CORCHETE_DERECHO)
        if not self.repetido('Arbol Registros'):
            self.nombres_arboles.append('Arbol Registros')
        
    def Bloque_Registros(self):
        if Token.LLAVE_IZQUIERDA == self.preanalisis:
            tmp = self.contador_registros
            self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "<CUERPO_REGISTROS>"];\n'
            self.contenido_registros += 'n'+str(self.contador_registros - 1)+' -> n'+str(self.contador_registros)+';\n'
            self.contador_registros += 1
            self.Cuerpo_Registros()
            if Token.LLAVE_IZQUIERDA == self.preanalisis:
                self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "<BLOQUE_REGISTROS>"];\n'
                self.contenido_registros += 'n'+str(tmp - 1)+' -> n'+str(self.contador_registros)+';\n'
                self.contador_registros += 1
            self.Bloque_Registros()
    
    def Cuerpo_Registros(self):
        tmp = self.contador_registros
        self.Match(Token.LLAVE_IZQUIERDA)
        self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "{"];\n'
        self.contenido_registros += 'n'+str(self.contador_registros - 1)+' -> n'+str(self.contador_registros)+';\n'
        self.contador_registros += 1
        
        self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "<VALOR_REGISTROS>"];\n'
        self.contenido_registros += 'n'+str(self.contador_registros - 2)+' -> n'+str(self.contador_registros)+';\n'
        self.contador_registros += 1
        
        self.valor_registro()
        self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "}"];\n'
        self.contenido_registros += 'n'+str(tmp - 1)+' -> n'+str(self.contador_registros)+';\n'
        self.contador_registros += 1
        self.Match(Token.LLAVE_DERECHA)
        self.guardar_registro()
              
    def valor_registro(self):
        if Token.NUMERO == self.preanalisis:
            nuevo = int(self.lista[self.posicion].lexema_valido)
            self.valores_registro.append(nuevo)
            self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "' + str(nuevo) + '"];\n'
            self.contenido_registros += 'n'+str(self.contador_registros - 1)+' -> n'+str(self.contador_registros)+';\n'
            self.contador_registros += 1
            self.Match(Token.NUMERO)
        elif Token.CADENA == self.preanalisis:
            nuevo = self.lista[self.posicion].lexema_valido
            nuevo = nuevo.replace('"','')
            self.valores_registro.append(nuevo)
            self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "' + nuevo + '"];\n'
            self.contenido_registros += 'n'+str(self.contador_registros - 1)+' -> n'+str(self.contador_registros)+';\n'
            self.contador_registros += 1
            self.Match(Token.CADENA)    
        elif Token.DECIMAL == self.preanalisis:
            nuevo = float(self.lista[self.posicion].lexema_valido)
            self.valores_registro.append(nuevo)
            self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "' +str(nuevo) + '"];\n'
            self.contenido_registros += 'n'+str(self.contador_registros - 1)+' -> n'+str(self.contador_registros)+';\n'
            self.contador_registros += 1
            self.Match(Token.DECIMAL)
        if Token.COMA == self.preanalisis:
            self.contenido_registros += 'n'+str(self.contador_registros)+'[label = ","];\n'
            self.contenido_registros += 'n'+str(self.contador_registros - 2)+' -> n'+str(self.contador_registros)+';\n'
            self.contador_registros += 1
            self.contenido_registros += 'n'+str(self.contador_registros)+'[label = "<VALOR_REGISTROS>"];\n'
            self.contenido_registros += 'n'+str(self.contador_registros - 3)+' -> n'+str(self.contador_registros)+';\n'
            self.contador_registros += 1
            self.Match(Token.COMA)
            self.valor_registro()
    
    def guardar_registro(self):
        if not self.entro_reg:
            self.tamano_val_registros = len(self.valores_registro)
            self.entro_reg = True
        values = self.valores_registro[self.valor_actual:self.valor_actual + self.tamano_val_registros]
        self.registros.agregar_registro(self.contador_registros, values)
        self.contador_registros += 1
        self.valor_actual += self.tamano_val_registros
    
    def arbol_registros(self):
        contenido = '''
        \r\t\tn1[label = "Registros"];
        \r\t\tn2[label = "="];
        \r\t\tn3[label = "["]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;'''
        contenido += self.contenido_registros
        return contenido
    
    def Comentario(self):
        comentario = self.lista[self.posicion].lexema_valido
        comentario = comentario.replace('\\','\\\\')
        self.Match(Token.COMENTARIO_LINEA)
        self.arboles.dic_arboles['comentario'] = comentario.replace('#','')
        if not self.repetido('Arbol Comentario Linea'):
            self.nombres_arboles.append('Arbol Comentario Linea')
    
    def Comentario_Multilinea(self):
        comentario = self.lista[self.posicion].lexema_valido
        comentario = comentario.replace('\\','\\\\')
        self.Match(Token.COMENTARIO_MULTILINEA)
        self.arboles.dic_arboles['comentario_multi'] = comentario.replace("'","")
        if not self.repetido('Arbol Comentario MultiLinea'):
            self.nombres_arboles.append('Arbol Comentario MultiLinea')
        
    def Imprimir(self):
        self.Match(Token.IMPRIMIR)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        print_consola = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA)         
        
        print_consola = print_consola.replace('"','')
        self.txt_consola.insert(self.tkinter.INSERT, print_consola)
        print_consola = print_consola.replace('\\','\\\\')
        self.arboles.dic_arboles['imprimir'] = print_consola
        if not self.repetido('Arbol Imprimir'):
            self.nombres_arboles.append('Arbol Imprimir')
        
    def ImprimirLn(self):
        self.Match(Token.IMPRIMIRLN)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        print_consola = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA) 
        
        print_consola = print_consola.replace('"','')
        self.txt_consola.insert(self.tkinter.INSERT, '\n' + print_consola + '\n') 
        print_consola = print_consola.replace('\\','\\\\')
        self.arboles.dic_arboles['imprimirln'] = print_consola
        if not self.repetido('Arbol ImprimirLn'):
            self.nombres_arboles.append('Arbol ImprimirLn') 
        
    def Conteo(self):
        self.Match(Token.CONTEO)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA)
        
        print_consola = len(self.registros.valores)
        self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(print_consola) + '\n')  
        if not self.repetido('Arbol Conteo'):
            self.nombres_arboles.append('Arbol Conteo')

    def Promedio(self):
        self.Match(Token.PROMEDIO)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        campo = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA) 
        campo = campo.replace('"','')
        self.obtener_promedio_suma(campo, True)
        self.arboles.dic_arboles['promedio'] = campo
        if not self.repetido('Arbol Promedio'):
            self.nombres_arboles.append('Arbol Promedio')
    
    def obtener_promedio_suma(self, campo, es_promedio):
        indice = -1
        suma = 0
        for claves in self.valores_clave:
            if claves.get_nombre() == campo:
                indice = claves.get_indice()
                break
        if indice != -1:
            for i in range(len(self.registros.valores)):
                suma += self.registros.valores[i].args[0][indice]
            if es_promedio and len(self.registros.valores) != 0:
                promedio = suma/len(self.registros.valores) 
                self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(promedio) + '\n')  
            else:
                self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(suma) + '\n')  
        else:
            self.txt_consola.insert(self.tkinter.INSERT, '>>> No se pudo encontrar el campo especificado\n')                 
        
    def ContarSi(self):
        self.Match(Token.CONTARSI)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        campo = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.COMA)   
        valor = self.valor_contarSi()
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)  
        campo = campo.replace('"','')        
        self.obtener_contar_si(campo, valor)
        self.arboles.dic_arboles['cadena_contar'] = campo
        self.arboles.dic_arboles['valor_contar'] = valor
        if not self.repetido('Arbol ContarSi'):
            self.nombres_arboles.append('Arbol ContarSi')
    
    def valor_contarSi(self): 
        if self.errorSintactico:
            return
        if Token.NUMERO == self.preanalisis:
            valor = self.lista[self.posicion].lexema_valido
            valor = int(valor)
            self.Match(Token.NUMERO)
            return valor  
        elif Token.DECIMAL == self.preanalisis:
            valor = self.lista[self.posicion].lexema_valido
            valor = float(valor)
            self.Match(Token.DECIMAL)
            return valor  
        elif Token.CADENA == self.preanalisis:
            dato: str = self.lista[self.posicion].lexema_valido
            dato = dato.replace('"',"")
            self.Match(Token.CADENA)
            return dato                        
        
    def obtener_contar_si(self, campo, valor): 
        if self.errorSintactico:
            return
        indice = -1
        contador = 0
        for claves in self.valores_clave:
            if claves.get_nombre() == campo:
                indice = claves.get_indice()
                break
        if indice != -1:
            for i in range(len(self.registros.valores)):
                if type(valor) == float:
                    if valor == float(self.registros.valores[i].args[0][indice]):
                        contador += 1
                elif type(valor) == int:  
                    if valor == int(self.registros.valores[i].args[0][indice]):
                        contador += 1
                elif type(valor) == str:  
                    if valor.replace(" ","").upper() == self.registros.valores[i].args[0][indice].replace(" ","").upper():
                        contador += 1              
            self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(contador)+'\n')   
        else:
            self.txt_consola.insert(self.tkinter.INSERT, '>>> No se pudo encontrar el campo especificado\n') 
        
    def arbol_contarsi(self):
        contenido = '''
        \r\t\tn1[label = "contarsi"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = "'''+self.arboles.dic_arboles.get('cadena_contar')+'''"];  
        \r\t\tn4[label = ","]; 
        \r\t\tn5[label = "<VALOR_CONTARSI>"];
        \r\t\tn6[label = "'''+str(self.arboles.dic_arboles.get('valor_contar'))+'''"];
        \r\t\tn7[label = ")"];       
        \r\t\tn8[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;
        \r\t\tn5 -> n6;
        \r\t\traiz -> n7;
        \r\t\traiz -> n8;'''
        return contenido
    
    def Datos(self):
        self.Match(Token.DATOS)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)   
        self.obtener_datos(False)  
        if not self.repetido('Arbol Datos'):
            self.nombres_arboles.append('Arbol Datos')          
    
    def obtener_datos(self, es_reporte):
        self.reporteHTML_registro += '<tr>'
        contenido = ''
        contador = 0
        for claves in self.valores_clave:
            contenido += claves.get_nombre().replace('_',' ')
            self.reporteHTML_registro += '<td align=center><font color=\"#000000\" face=\"Courier\"><strong>'+claves.get_nombre().replace('_',' ')+'</strong></td>'
            contador += 1
            if contador != len(self.valores_clave):
                contenido += ' - '       
        contenido += '\n'    
        contador = 0
        self.reporteHTML_registro += '</tr>'
        
        for i in range(len(self.registros.valores)):
            self.reporteHTML_registro += '<tr>'
            for claves in self.valores_clave:
                contenido += str(self.registros.valores[i].args[0][claves.get_indice()])
                self.reporteHTML_registro += '<td align=center><font color=\"#000000\" face=\"Courier\">'+str(self.registros.valores[i].args[0][claves.get_indice()])+'</td>'
                contador += 1
                if contador != len(self.valores_clave):
                    contenido += ' - '
                else:
                    contador = 0
            self.reporteHTML_registro += '</tr>'
            contenido += '\n'  
         
        if not es_reporte:     
            self.txt_consola.insert(self.tkinter.INSERT, contenido+'\n')
            self.reporteHTML_registro = ''
    
    def Sumar(self):
        self.Match(Token.SUMAR)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        campo = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)  
        campo = campo.replace('"','')
        self.obtener_promedio_suma(campo, False)
        self.arboles.dic_arboles['sumar'] = campo
        if not self.repetido('Arbol Sumar'):
            self.nombres_arboles.append('Arbol Sumar')
    
    def Max(self):
        self.Match(Token.MAX)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        campo = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)  
        campo = campo.replace('"','')
        self.obtener_max_min(campo, True)
        self.arboles.dic_arboles['max'] = campo
        if not self.repetido('Arbol Max'):
            self.nombres_arboles.append('Arbol Max')
        
    def obtener_max_min(self, campo, es_max):
        indice = -1
        maximo = 0
        minimo = 100000000000
        tmp = 0
        for claves in self.valores_clave:
            if claves.get_nombre() == campo:
                indice = claves.get_indice()
                break
        if indice != -1:
            for i in range(len(self.registros.valores)):
                tmp = float(self.registros.valores[i].args[0][indice])
                if tmp > maximo:
                    maximo = tmp
                if tmp < minimo:
                    minimo = tmp 
            if es_max:               
                self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(maximo) + '\n')
            else:
                if minimo == 100000000000:
                    self.txt_consola.insert(self.tkinter.INSERT, '>>> 0\n')   
                else:
                    self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(minimo) + '\n')         
        else:
            self.txt_consola.insert(self.tkinter.INSERT, '>>> No se pudo encontrar el campo especificado\n') 
               
    def Min(self):
        self.Match(Token.MIN)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        campo = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)  
        campo = campo.replace('"','') 
        self.obtener_max_min(campo, False)  
        self.arboles.dic_arboles['min'] = campo
        if not self.repetido('Arbol Min'):
            self.nombres_arboles.append('Arbol Min') 
        
    def Exportar_Reporte(self):
        self.Match(Token.EXPORTARREPORTE)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        nombre = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)   
        nombre = nombre.replace('"','')    
        self.crear_reporte_registro(nombre)
        self.arboles.dic_arboles['reporte'] = nombre
        if not self.repetido('Arbol Exportar Reporte'):
            self.nombres_arboles.append('Arbol Exportar Reporte')
    
    def reniciar(self):
        self.lista.clear()
        self.valores_registro.clear()
        self.registros.reiniciar_registro()
        self.valores_clave.clear()
        self.nombres_arboles.clear()
    
    def opciones_reporte_arbol(self, combo_reportes):        
        combo_reportes["values"] = ["Seleccione el Reporte", "Reporte Tokens", "Reporte Errores Léxico", "Reporte Error Sintáctico"]        
        values = list(combo_reportes["values"])   
        combo_reportes["values"] = values + self.nombres_arboles
    
    def repetido(self, nombre_entrada):
        for nombres in self.nombres_arboles:
            if nombres == nombre_entrada:
                return True
        return False
               
    def Repetir(self):
        if Token.CLAVES == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<CLAVES>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Claves()
            self.Repetir()
        elif Token.REGISTROS == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REGISTROS>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Registros()
            self.Repetir()
        elif Token.COMENTARIO_LINEA == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<C0MENTARIO_LINEA>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Comentario()
            self.Repetir()    
        elif Token.COMENTARIO_MULTILINEA == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<COMENTARIO_MULTILINEA>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Comentario_Multilinea()
            self.Repetir()     
        elif Token.IMPRIMIR == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<IMPRIMIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Imprimir()
            self.Repetir()
        elif Token.IMPRIMIRLN == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<IMPRIMIRLN>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.ImprimirLn()
            self.Repetir()
        elif Token.CONTEO == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<CONTEO>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Conteo()
            self.Repetir()
        elif Token.PROMEDIO == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<PROMEDIO>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Promedio()
            self.Repetir()
        elif Token.CONTARSI == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<CONTARSI>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.ContarSi()
            self.Repetir()
        elif Token.DATOS == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<DATOS>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Datos()
            self.Repetir()
        elif Token.SUMAR == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<SUMAR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Sumar()
            self.Repetir()
        elif Token.MAX == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<MAX>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Max()
            self.Repetir()
        elif Token.MIN == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<MIN>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Min()
            self.Repetir()
        elif Token.EXPORTARREPORTE == self.preanalisis:
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<REPETIR>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 2)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.contenido_inicio += 'n'+str(self.contador_inicio)+'[label = "<EXTRAERREPORTE>"];\n'
            self.contenido_inicio += 'n'+str(self.contador_inicio - 1)+' -> n'+str(self.contador_inicio)+';\n'
            self.contador_inicio += 1
            self.Exportar_Reporte()
            self.Repetir()
        else:
            if not self.repetido('Arbol Inicio'):
                self.nombres_arboles.append('Arbol Inicio')
                
    def crear_reporte_registro(self, nombre):
        makedirs('Reportes', exist_ok = True)
        self.obtener_datos(True)
        try: 
            file = open('Reportes/' + nombre + '.html','w')
            head = '<head><title>Reporte Registro</title></head>\n'
            body = '''<body bgcolor=\"#B6F49D\">
                    <table width=\"600\" bgcolor=#B6F49D align=left> <tr> <td><font color=\"black\" FACE=\"Courier\">
                    <p align=\"left\">Arnoldo Luis Antonio González Camey &nbsp;—&nbsp; Carné: 201701548</p></font>
                    </td> </tr></table></br></br>'''
            body += '<h2 align=\"center\"><font color=\"black\" FACE=\"Courier\">'+nombre+'</h2>'
            body += '<table width=\"1000\" bgcolor=#CDF9BA align=center style="border:5px dashed brown">'
            body += self.reporteHTML_registro +'</table></body>'
            html = '<html>\n' + head + body + '</html>'
            file.write(html)
            print('Reporte de Registro generado exitosamente')
        except OSError:
            print("Error al crear el Reporte de Registro")
        finally:         
            file.close()
            webbrowser.open_new_tab('Reportes\\' + nombre + '.html')        
    
    def crear_reporte_errores_sintactico(self):
        makedirs('Reportes', exist_ok = True)
        try: 
            file = open('Reportes/Reporte_Errores_Sintactico.html','w')
            head = '<head><title>Reporte Errores Sintácticos</title></head>\n'
            body = '''<body bgcolor=\"#B6F49D\">
                    <table width=\"600\" bgcolor=#B6F49D align=left> <tr> <td><font color=\"black\" FACE=\"Courier\">
                    <p align=\"left\">Arnoldo Luis Antonio González Camey &nbsp;—&nbsp; Carné: 201701548</p></font>
                    </td> </tr></table></br></br>
                    <h2 align=\"center\"><font color=\"black\" FACE=\"Courier\">Tabla Errores Sintáctico</h2>
                    <table width=\"1250\" bgcolor=#CDF9BA align=center style="border:5px dashed brown">
                    <tr>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Error Lexema</strong></td>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Error</strong></td>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Fila</strong></td>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Columna</strong></td>    
                    </tr>''' 
            body += self.reporte_error_sintac +'</table></body>'
            html = '<html>\n' + head + body + '</html>'
            file.write(html)
            print('Reporte de errores sintácticos generado exitosamente')
        except OSError:
            print("Error al crear el Reporte de errores sintácticos")
        finally:         
            file.close()
            webbrowser.open_new_tab('Reportes\Reporte_Errores_Sintactico.html')