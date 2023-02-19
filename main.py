class asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self, color):
        if color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco":
            self.color=color

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro= registro

    def cantidadAsientos(self):
        canasi= 0
        if None != self.asientos:
            for asientos in self.asientos:
                if asientos != None:
                    canasi += 1
        return canasi

    def verificarIntegridad (self):
        AutoOr= "Auto original"
        AutoRe= "Las piezas no son originales"
        if self.registro == self.asientos[0].registro:
            if self.motor.registro == self.registro:
                return AutoOr
            else:
                return AutoRe
        return AutoRe

class Motor:
    def __int__(self,numeroCilindros, tipo, registro):
        self.numeroCilindros= numeroCilindros
        self.tipo= tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        self.registro=registro

    def asignarTipo(self,tipo):
        if tipo=="Gasolina" or tipo== electrico:
            self.tipo=tipo