from Token import Token
import re
import webbrowser

class Analizador():
    
    reporteHTML_token = ''
    reporteHTML_errores = ''
    lexema = ''
    estado = 0
    tokens = []
    columna = 1
    fila = 1
    id = 0
    tipos = Token("lexema", -1, -1, -1, -1)
    
    def agregar_token(self, tipo):
        nuevo_token = Token(self.lexema, tipo, self.fila, self.columna, self.id)
        self.tokens.append(nuevo_token)
        self.lexema = ''
        self.estado = 0
        if tipo != 28:
            self.id += 1
            
    def analizador_estados(self, entrada):
        self.estado = 0
        self.lexema = ''
        self.tokens = []
        self.fila = 1
        self.columna = 1
        #entrada = self.quitar_espacios(entrada)
        entrada = self.separar(entrada)
        entrada += '`'
        #print(entrada)
        actual = ''
        longitud = len(entrada)
        for contador in range(longitud):
            actual = entrada[contador]
            if self.estado == 0:
                if actual.isalpha():
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                     
                elif actual.isdigit():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                
                elif actual == '"':
                    self.estado = 3
                    self.columna += 1                    
                    self.lexema += actual   
                
                elif actual == '=':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.IGUAL)
                
                elif actual == '[':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.CORCHETE_IZQUIERDO)
                    
                elif actual == ']':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.CORCHETE_DERECHO)
                
                elif actual == '(':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.PARENTESIS_IZQUIERDO)
                
                elif actual == ')':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.PARENTESIS_DERECHO) 
                
                elif actual == '{':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.LLAVE_IZQUIERDA) 
                    
                elif actual == '}':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.LLAVE_DERECHA)     
                    
                elif actual == ',':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.COMA)    
                       
                elif actual == ';':
                    self.columna += 1  
                    self.lexema += actual                    
                    self.agregar_token(self.tipos.PUNTO_Y_COMA)       
                
                elif actual == "'":
                    self.estado = 5
                    self.columna += 1                    
                    self.lexema += actual
                     
                elif actual == '#':
                    self.estado = 6
                    self.columna += 1                    
                    self.lexema += actual    
                     
                elif actual == ' ':
                    self.columna +=1
                    self.estado = 0
                     
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 0
                    self.columna = 1
                     
                elif actual =='\r':
                    self.estado = 0
                     
                elif actual == '\t':
                    self.columna += 5
                    self.estado = 0
                     
                elif actual == '`' and contador == longitud - 1:
                    self.lexema = '`'
                    self.agregar_token(self.tipos.ULTIMO)
                    print('Análisis terminado')
                    
                else:
                    self.lexema += actual
                    self.agregar_token(self.tipos.ERROR)
                    self.columna += 1  
            
            elif self.estado == 1:
                if actual.isalpha():
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                else:
                    if not self.es_palabra_reserva(self.lexema):
                        self.agregar_token(self.tipos.ERROR)
                        
            elif self.estado == 2:
                if actual.isdigit():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                elif actual == '.':
                    self.estado = 7
                    self.columna += 1
                    self.lexema += actual    
                else:
                    self.agregar_token(self.tipos.NUMERO)
                    
            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.columna +=1
                    self.lexema += actual
                     
                elif actual == '"':
                    self.estado = 8
                    self.lexema += actual 
                    self.agregar_token(self.tipos.CADENA)                             
                                
            elif self.estado == 5:
                if actual == "'":
                    self.estado = 9
                    self.columna += 1
                    self.lexema += actual
        
                else:
                    self.agregar_token(self.tipos.ERROR)  
            
            elif self.estado == 6:
                if actual == '\n':
                    self.fila += 1
                    self.estado = 0
                    self.columna = 1
                    self.agregar_token(self.tipos.COMENTARIO_LINEA)
                else:
                    self.estado = 6
                    self.columna += 1
                    self.lexema += actual       
            
            elif self.estado == 7:
                if actual.isdigit():
                    self.estado = 10
                    self.columna += 1
                    self.lexema += actual
                else:
                    self.agregar_token(self.tipos.ERROR)  
            
            elif self.estado == 9:
                if actual == "'":
                    self.estado = 11
                    self.columna += 1
                    self.lexema += actual
                else:
                    self.agregar_token(self.tipos.ERROR)  
                    
            elif self.estado == 10:
                if actual.isdigit():
                    self.estado = 10
                    self.columna += 1
                    self.lexema += actual
                else:
                    self.agregar_token(self.tipos.DECIMAL)   
            
            elif self.estado == 11:
                if actual != "'":
                    self.estado = 11
                    self.columna += 1
                    self.lexema += actual 
                else:
                    self.estado = 12
                    self.columna += 1
                    self.lexema += actual   
                       
            elif self.estado == 12:
                if actual == "'":
                    self.estado = 13
                    self.columna += 1
                    self.lexema += actual  
                else:
                    self.agregar_token(self.tipos.ERROR)     
            
            elif self.estado == 13:
                if actual == "'":
                    self.estado = 14
                    self.columna += 1
                    self.lexema += actual
                    self.agregar_token(self.tipos.COMENTARIO_MULTILINEA) 
                else:
                    self.agregar_token(self.tipos.ERROR)  
        
    def separar(self, entrada):
        #patron = r'(\w)([,-;-{-}-(-)-\[-\]-\=])'
        patron = r'(\w)([= - { - } - , - ; - ( - ) - \[ - \] ])'
        return re.sub(patron, r'\1 \2 ', entrada)                           
    
    def quitar_espacios(self, entrada):
        patron = ' +'#hacer que quite los espacios en solo esos que me interesa los  = [ ] etc
        return re.sub(patron, '', entrada)
    
    def es_palabra_reserva(self, entrada):
        entrada = entrada.upper()
        if entrada == 'CLAVES':
            self.agregar_token(self.tipos.CLAVES)
            return True
        if entrada == 'REGISTROS':
            self.agregar_token(self.tipos.REGISTROS)
            return True
        if entrada == 'IMPRIMIR':
            self.agregar_token(self.tipos.IMPRIMIR)
            return True
        if entrada == 'IMPRIMIRLN':
            self.agregar_token(self.tipos.IMPRIMIRLN)
            return True
        if entrada == 'CONTEO':
            self.agregar_token(self.tipos.CONTEO)
            return True
        if entrada == 'PROMEDIO':
            self.agregar_token(self.tipos.PROMEDIO)
            return True
        if entrada == 'CONTARSI':
            self.agregar_token(self.tipos.CONTARSI)
            return True
        if entrada == 'DATOS':
            self.agregar_token(self.tipos.DATOS)
            return True
        if entrada == 'SUMAR':
            self.agregar_token(self.tipos.SUMAR)
            return True
        if entrada == 'MAX':
            self.agregar_token(self.tipos.MAX)
            return True
        if entrada == 'MIN':
            self.agregar_token(self.tipos.MIN)
            return True
        if entrada == 'EXPORTARREPORTE':
            self.agregar_token(self.tipos.EXPORTARREPORTE)
            return True
        return False
   
    def opciones_imagenes(self, combo):
        nombres = []
        values = list(combo["values"])
        for img in self.imagenes:
            nombres.append(img.titulo) 
        combo["values"] = values + nombres
    
    def obtener_tokens(self):
        font = '<font color=\"#000000\" face=\"Courier\">'
        for x in self.tokens:
            if x.tipo != self.tipos.ERROR:
                self.reporteHTML_token += '<tr><td align=center>'+ font + x.get_tipo() + '</td><td align=center>'+ font + x.get_lexema() + '</td><td align=center>'+ font + str(x.get_fila()) + '</td><td align=center>'+ font + str(x.get_columna()) + '</td></tr>'
                print(x.get_lexema()," --> ",x.get_tipo(),' --> ',x.get_fila(), ' --> ',x.get_columna(), ' --> ',x.get_id())
    
    def obtener_errores(self):
        font = '<font color=\"#000000\" face=\"Courier\">'
        for x in self.tokens:
            if x.tipo == self.tipos.ERROR:
                self.reporteHTML_errores += '<tr><td align=center>'+ font + x.get_lexema() + '</td><td align=center>'+ font + str(x.get_fila()) + '</td><td align=center>'+ font + str(x.get_columna()) + '</td></tr>'
                print(x.get_lexema()," --> ",x.get_fila(), ' --> ',x.get_columna(),'--> Error Lexico')                                      
     
    def crear_reporte_token(self):
        try: 
            file = open('Reporte_Tokens.html','w')
            head = '<head><title>Reporte Token</title></head>\n'
            body = "<body bgcolor=\"#B6F49D\">"
            body += "<table width=\"600\" bgcolor=#B6F49D align=left> <tr> <td><font color=\"black\" FACE=\"Courier\">" 
            body += "<p align=\"left\">Arnoldo Luis Antonio González Camey &nbsp;—&nbsp; Carné: 201701548</p></font>"
            body += "</td> </tr></table></br></br>"
            body += ''' <h2 align=\"center\"><font color=\"black\" FACE=\"Courier\">Reporte de Tokens</h2>
                    <table width=\"1000\" bgcolor=#CDF9BA align=center style="border:5px dashed brown">
                    <tr>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Token</strong></td>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Lexema</strong></td>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Fila</strong></td>                                            
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Columna</strong></td>
                    </tr>''' 
            body += self.reporteHTML_token +'</table></body>'
            html = '<html>\n' + head + body + '</html>'
            file.write(html)
            print('Reporte de Tokens generado exitosamente')
        except OSError:
            print("Error al crear el Reporte de Tokens")
        finally:         
            file.close()
            webbrowser.open_new_tab('Reporte_Tokens.html')
        
    def crear_reporte_errores(self):
        try: 
            file = open('Reporte_Errores.html','w')
            head = '<head><title>Reporte Errores</title></head>\n'
            body = "<body bgcolor=\"#B6F49D\">"
            body += "<table width=\"600\" bgcolor=#B6F49D align=left> <tr> <td><font color=\"black\" FACE=\"Courier\">" 
            body += "<p align=\"left\">Arnoldo Luis Antonio González Camey &nbsp;—&nbsp; Carné: 201701548</p></font>"
            body += "</td> </tr></table></br></br>"
            body += ''' <h2 align=\"center\"><font color=\"black\" FACE=\"Courier\">Reporte de Errores</h2>
                    <table width=\"800\" bgcolor=#CDF9BA align=center style="border:5px dashed brown">
                    <tr>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Caracter</strong></td>
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Fila</strong></td>                                            
                        <td align=center><font color=\"#000000\" face=\"Courier\"><strong>Columna</strong></td>
                    </tr>''' 
            body += self.reporteHTML_errores +'</table></body>'
            html = '<html>\n' + head + body + '</html>'
            file.write(html)
            print('Reporte de Errores generado exitosamente')
        except OSError:
            print("Error al crear el Reporte de Errores")
        finally:         
            file.close()
            webbrowser.open_new_tab('Reporte_Errores.html')