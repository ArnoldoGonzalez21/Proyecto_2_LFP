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
        if not self.repetido('Arbol Claves'):
            self.nombres_arboles.append('Arbol Claves')

    def Cuerpo_Claves(self):
        if Token.CADENA == self.preanalisis:
            nombre = self.lista[self.posicion].lexema_valido
            nombre = nombre.replace('"','')
            nuevo = Clave(self.indice_clave, nombre)
            self.valores_clave.append(nuevo)
            self.indice_clave += 1
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
        if not self.repetido('Arbol Registros'):
            self.nombres_arboles.append('Arbol Registros')
        
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
            self.tamano_val_registros = len(self.valores_registro)
            self.entro_reg = True
        values = self.valores_registro[self.valor_actual:self.valor_actual + self.tamano_val_registros]
        self.registros.agregar_registro(self.contador_registros, values)
        self.contador_registros += 1
        self.valor_actual += self.tamano_val_registros
              
    def valor_registro(self):
        if Token.NUMERO == self.preanalisis:
            nuevo = self.lista[self.posicion].lexema_valido
            self.valores_registro.append(nuevo)
            self.Match(Token.NUMERO)
        elif Token.CADENA == self.preanalisis:
            nuevo = self.lista[self.posicion].lexema_valido
            nuevo = nuevo.replace('"','')
            self.valores_registro.append(nuevo)
            self.Match(Token.CADENA)    
        elif Token.DECIMAL == self.preanalisis:
            nuevo = self.lista[self.posicion].lexema_valido
            self.valores_registro.append(nuevo)
            self.Match(Token.DECIMAL)
        if Token.COMA == self.preanalisis:
            self.Match(Token.COMA)
            self.valor_registro()
    
    def Comentario(self):
        self.Match(Token.COMENTARIO_LINEA)
        if not self.repetido('Arbol Comentario Linea'):
            self.nombres_arboles.append('Arbol Comentario Linea')
    
    def Comentario_Multilinea(self):
        self.Match(Token.COMENTARIO_MULTILINEA)
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
        if not self.repetido('Arbol ImprimirLn'):
            self.nombres_arboles.append('Arbol ImprimirLn') 
        
    def Conteo(self):
        self.Match(Token.CONTEO)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        self.Match(Token.PARENTESIS_DERECHO)
        self.Match(Token.PUNTO_Y_COMA)
        
        print_consola = len(self.registros.valores)
        self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(print_consola))  
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
                suma += int(self.registros.valores[i].args[0][indice])
        if es_promedio and len(self.registros.valores) != 0:
            promedio = suma/len(self.registros.valores) 
            self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(promedio))  
        else:
            self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(suma))   
        
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
        if not self.repetido('Arbol ContarSi'):
            self.nombres_arboles.append('Arbol ContarSi')
    
    def valor_contarSi(self):
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
                contenido += self.registros.valores[i].args[0][claves.get_indice()]
                self.reporteHTML_registro += '<td align=center><font color=\"#000000\" face=\"Courier\">'+self.registros.valores[i].args[0][claves.get_indice()]+'</td>'
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
        if not self.repetido('Arbol Max'):
            self.nombres_arboles.append('Arbol Max')
        
    def obtener_max_min(self, campo, es_max):
        indice = -1
        maximo = 0
        minimo = 100000
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
            self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(maximo))
        else:
            self.txt_consola.insert(self.tkinter.INSERT, '>>> ' + str(minimo))    
        
    def Min(self):
        self.Match(Token.MIN)
        self.Match(Token.PARENTESIS_IZQUIERDO)
        campo = self.lista[self.posicion].lexema_valido
        self.Match(Token.CADENA)
        self.Match(Token.PARENTESIS_DERECHO)     
        self.Match(Token.PUNTO_Y_COMA)  
        campo = campo.replace('"','') 
        self.obtener_max_min(campo, False)  
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
        for i in self.nombres_arboles:
            print(i)
    
    def repetido(self, nombre_entrada):
        for nombres in self.nombres_arboles:
            if nombres == nombre_entrada:
                return True
        return False
    
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
        else:
            if not self.repetido('Arbol Inicio'):
                self.nombres_arboles.append('Arbol Inicio')