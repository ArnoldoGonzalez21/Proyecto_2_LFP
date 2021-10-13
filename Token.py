class Token():
    
    lexema_valido = ''
    tipo = 0
    fila = 0
    columna = 0
    
    CLAVES = 1
    REGISTROS = 2
    IMPRIMIR = 3
    IMPRIMIRLN = 4
    CONTEO = 5
    PROMEDIO = 6
    CONTARSI = 7
    DATOS = 8
    SUMAR = 9
    MAX = 10
    MIN = 11 
    EXPORTARREPORTE = 12
    LETRA = 13
    NUMERO = 14
    CADENA = 15    
    IGUAL = 16
    CORCHETE_IZQUIERDO = 17
    CORCHETE_DERECHO = 18
    PUNTO_Y_COMA = 19
    PARENTESIS_IZQUIERDO = 20
    PARENTESIS_DERECHO = 21
    LLAVE_IZQUIERDA = 22
    LLAVE_DERECHA = 23
    COMA = 24
    COMENTARIO_MULTILINEA = 25
    COMENTARIO_LINEA = 26
    DECIMAL = 27
    ERROR = 28
    ULTIMO = 29
    
    def __init__(self, lexema, tipo, fila, columna, id):
        self.lexema_valido = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.id = id
       
    def get_tipo(self):
        if self.tipo == self.CLAVES or self.tipo == self.REGISTROS or self.tipo == self.IMPRIMIR or self.tipo == self.IMPRIMIRLN: 
            return 'Palabra Reservada'
        elif self.tipo == self.CONTEO or self.tipo == self.PROMEDIO or self.tipo == self.CONTARSI or self.tipo == self.DATOS:
            return 'Palabra Reservada'
        elif self.tipo == self.SUMAR or self.tipo == self.MAX or self.tipo == self.MIN or self.tipo == self.EXPORTARREPORTE: 
            return 'Palabra Reservada'
        elif self.tipo == self.LETRA:
            return 'Letra'
        elif self.tipo == self.NUMERO:
            return 'Número'
        elif self.tipo == self.CADENA:
            return 'Cadena'
        elif self.tipo == self.IGUAL or self.tipo == self.CORCHETE_IZQUIERDO or self.tipo == self.CORCHETE_DERECHO:
            return 'Signo'
        elif self.tipo == self.PUNTO_Y_COMA or self.tipo == self.PARENTESIS_IZQUIERDO or self.tipo == self.PARENTESIS_DERECHO:
            return 'Signo'
        elif self.tipo == self.COMA or self.tipo == self.LLAVE_DERECHA or self.tipo == self.LLAVE_IZQUIERDA:
            return 'Signo'
        elif self.tipo == self.COMENTARIO_MULTILINEA:
            return 'Comentario Multilinea'
        elif self.tipo == self.COMENTARIO_LINEA:
            return 'Comentario una Linea'
        elif self.tipo == self.DECIMAL:
            return 'Decimal'
        elif self.tipo == self.ULTIMO:
            return 'Ultimo'
    
    def get_lexema(self):
        return self.lexema_valido 
       
    def get_fila(self):
        return self.fila   
    
    def get_columna(self):
        return self.columna
    
    def get_id(self):
        return self.id 