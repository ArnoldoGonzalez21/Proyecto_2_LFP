class Registro():
    valores = []
    def __init__(self, indice, *args):
        self.indice = indice
        self.args = args
        
    def agregar_registro(self, indice, values):
        nuevo = Registro(indice, values)
        self.valores.append(nuevo)       