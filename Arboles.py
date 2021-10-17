from os import system, startfile, makedirs

class Arboles():
    
    dic_arboles = {'comentario': '', 'comentario_multi':'', 'imprimir':'', 'imprimirln':'','cadena_contar':'','valor_contar':'','promedio':'','sumar':'', 'max':'', 'min':'','reporte':''}
    
    def arbol_comentario_linea(self):
        contenido = '''
        \r\t\tn1[label = "'''+self.dic_arboles.get('comentario')+'''"];
        \r\t\traiz -> n1;'''
        return contenido
    
    def arbol_comentario_multilinea(self):
        contenido = '''
        \r\t\tn1[label = "'''+self.dic_arboles.get('comentario_multi')+'''"];
        \r\t\traiz -> n1;'''
        return contenido
    
    def arbol_imprimir(self):
        contenido = '''
        \r\t\tn1[label = "imprimir"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = "'''+self.dic_arboles.get('imprimir')+'''"];
        \r\t\tn4[label = ")"];       
        \r\t\tn5[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_imprimirln(self):
        contenido = '''
        \r\t\tn1[label = "imprimirln"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = "'''+self.dic_arboles.get('imprimirln')+'''"];  
        \r\t\tn4[label = ")"];       
        \r\t\tn5[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_conteo(self):
        contenido = '''
        \r\t\tn1[label = "conteo"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = ")"];       
        \r\t\tn4[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;'''
        return contenido
    
    def arbol_promedio(self):
        contenido = '''
        \r\t\tn1[label = "promedio"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = "'''+self.dic_arboles.get('promedio')+'''"];   
        \r\t\tn4[label = ")"];       
        \r\t\tn5[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_datos(self):
        contenido = '''
        \r\t\tn1[label = "datos"];
        \r\t\tn2[label = "("];  
        \r\t\tn3[label = ")"];       
        \r\t\tn4[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;'''
        return contenido
    
    def arbol_sumar(self):
        contenido = '''
        \r\t\tn1[label = "sumar"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = "'''+self.dic_arboles.get('sumar')+'''"];  
        \r\t\tn4[label = ")"];       
        \r\t\tn5[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_max(self):
        contenido = '''
        \r\t\tn1[label = "max"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = "'''+self.dic_arboles.get('max')+'''"];  
        \r\t\tn4[label = ")"];       
        \r\t\tn5[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_min(self):
        contenido = '''
        \r\t\tn1[label = "min"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = "'''+self.dic_arboles.get('min')+'''"];   
        \r\t\tn4[label = ")"];       
        \r\t\tn5[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def arbol_exportar_reporte(self):
        contenido = '''
        \r\t\tn1[label = "exportarReporte"];
        \r\t\tn2[label = "("]; 
        \r\t\tn3[label = "'''+self.dic_arboles.get('reporte')+'''"];   
        \r\t\tn4[label = ")"];       
        \r\t\tn5[label = ";"]; 
        \r\t\traiz -> n1;
        \r\t\traiz -> n2;
        \r\t\traiz -> n3;
        \r\t\traiz -> n4;
        \r\t\traiz -> n5;'''
        return contenido
    
    def generar_graphviz_arbol(self, nombre_token, contenido, nombre_raiz):
        inicio_graphviz = '''
        \rdigraph L {
        \r\tnode[shape = box fillcolor = "#FFFF00" style = filled]
        \r\tsubgraph cluster_p {
        \r\t\tlabel = "Arbol Derivacion - '''+ nombre_token.replace("_", " ") +''' "
        \r\t\tbgcolor = "#6BD6E9"
        \r\t\t'''+nombre_raiz+'''[label = "<'''+nombre_token.upper()+'''>"]'''
        final_graphviz = '\n\t}\n}'
        graphviz = inicio_graphviz + contenido + final_graphviz
        makedirs('Reportes', exist_ok = True)
        miArchivo = open('Reportes/'+nombre_token+'.dot','w')
        miArchivo.write(graphviz)
        miArchivo.close()
        system('dot -Tpng ' +'Reportes/'+nombre_token+'.dot -o '+'Reportes/'+nombre_token+'.png')
        system('cd ./'+'Reportes/'+nombre_token+'.png')
        startfile('Reportes\\'+nombre_token+'.png')