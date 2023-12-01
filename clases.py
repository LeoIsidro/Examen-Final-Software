
class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.historial = []

    def getNumero(self):
        return self.numero

    def getNombre(self):
        return self.nombre

    def getSaldo(self):
        return self.saldo

    def getContactos(self):
        return self.contactos

    def setNumero(self, numero):
        self.numero = numero

    def setNombre(self, nombre):
        self.nombre = nombre

    def setSaldo(self, saldo):
        self.saldo = saldo

    def setContactos(self, contactos):
        self.contactos = contactos

    def agregarContacto(self, contacto):
        self.contactos.append(contacto)

    def eliminarContacto(self, contacto):
        self.contactos.remove(contacto)

    def historial_transacciones(self):
        return self.historial
    
    def pagar(self, numero, monto):
        self.saldo = self.saldo - monto
        self.historial.append(Operacion(numero, monto,"pago"))

    def recibir(self, numero, monto):
        self.saldo = self.saldo + monto
        self.historial.append(Operacion(numero, monto,"recibo"))        
        

class Operacion:
    def __init__(self, NumeroDestino, Valor,tipo):
        self.NumeroDestino = NumeroDestino
        self.Valor = Valor
        self.tipo=tipo
