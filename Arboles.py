from os import system, startfile, makedirs

class Arboles():
    
    def arbol_comentario_linea(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Comentario_Linea"];
        \r\t\traiz -> n1;'''
        return contenido
    
    def arbol_comentario_multilinea(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Comentario_Multilinea"];
        \r\t\traiz -> n1;'''
        return contenido
    
    def arbol_imprimir(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Imprimir"];
        \r\t\tn2[label = "Tk_Paren_Izq"]; 
        \r\t\tn3[label = "Tk_Cadena"];   
        \r\t\tn4[label = "Tk_Paren_Der"];       
        \r\t\tn5[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_imprimirln(self):
        contenido = '''
        \r\t\tn1[label = "Tk_ImprimirLn"];
        \r\t\tn2[label = "Tk_Paren_Izq"]; 
        \r\t\tn3[label = "Tk_Cadena"];   
        \r\t\tn4[label = "Tk_Paren_Der"];       
        \r\t\tn5[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_conteo(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Conteo"];
        \r\t\tn2[label = "Tk_Paren_Izq"]; 
        \r\t\tn3[label = "Tk_Paren_Der"];       
        \r\t\tn4[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;'''
        return contenido
    
    def arbol_promedio(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Promedio"];
        \r\t\tn2[label = "Tk_Paren_Izq"]; 
        \r\t\tn3[label = "Tk_Cadena"];   
        \r\t\tn4[label = "Tk_Paren_Der"];       
        \r\t\tn5[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_datos(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Datos"];
        \r\t\tn2[label = "Tk_Paren_Izq"];  
        \r\t\tn3[label = "Tk_Paren_Der"];       
        \r\t\tn4[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;'''
        return contenido
    
    def arbol_sumar(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Sumar"];
        \r\t\tn2[label = "Tk_Paren_Izq"]; 
        \r\t\tn3[label = "Tk_Cadena"];   
        \r\t\tn4[label = "Tk_Paren_Der"];       
        \r\t\tn5[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_max(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Max"];
        \r\t\tn2[label = "Tk_Paren_Izq"]; 
        \r\t\tn3[label = "Tk_Cadena"];   
        \r\t\tn4[label = "Tk_Paren_Der"];       
        \r\t\tn5[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_min(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Min"];
        \r\t\tn2[label = "Tk_Paren_Izq"]; 
        \r\t\tn3[label = "Tk_Cadena"];   
        \r\t\tn4[label = "Tk_Paren_Der"];       
        \r\t\tn5[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_exportar_reporte(self):
        contenido = '''
        \r\t\tn1[label = "Tk_Exp_Repo"];
        \r\t\tn2[label = "Tk_Paren_Izq"]; 
        \r\t\tn3[label = "Tk_Cadena"];   
        \r\t\tn4[label = "Tk_Paren_Der"];       
        \r\t\tn5[label = "Tk_Punto_Coma"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def generar_graphviz_arbol(self, nombre_token, contenido):
        inicio_graphviz = '''
        \rdigraph L {
        \r\tnode[shape = box fillcolor = "#FFFF00" style = filled]
        \r\tsubgraph cluster_p {
        \r\t\tlabel = "Arbol Derivacion - '''+ nombre_token.replace("_", " ") +''' "
        \r\t\tbgcolor = "#6BD6E9"
        \r\t\traiz[label = "<'''+nombre_token.upper()+'''>"]'''
        final_graphviz = '\n\t}\n}'
        graphviz = inicio_graphviz + contenido + final_graphviz
        makedirs('Reportes', exist_ok = True)
        miArchivo = open('Reportes/'+nombre_token+'.dot','w')
        miArchivo.write(graphviz)
        miArchivo.close()
        system('dot -Tpng ' +'Reportes/'+nombre_token+'.dot -o '+'Reportes/'+nombre_token+'.png')
        system('cd ./'+'Reportes/'+nombre_token+'.png')
        startfile('Reportes\\'+nombre_token+'.png')
          