
class ABB():
    def __init__(self):
        self.node = None

    def agregarAux(self, a, nombre, apellido, celular, correo):
        if apellido < a.getApellido():
            if a.getLeft() == None:
                a.setLeft(contacto(nombre,apellido,celular, correo))
                return
            self.agregarAux(a.getLeft(),nombre,apellido,celular, correo)
        else:
            if a.getRight() == None:
                a.setRight(contacto(nombre,apellido,celular, correo))
                return
            self.agregarAux(a.getRight(), nombre,apellido,celular, correo)

    def insertar(self,nombre,apellido,telefono,mail):
        if self.node == None:
            self.node = contacto(nombre,apellido,celular, correo)
        self.agregarAux(self.node,nombre,apellido,celular, correo)

    def inorder_aux(self, aux):
        if aux == None:
            return None
        else:
            self.inorder_aux(aux.getLeft())
            print(aux.getApellido())
            self.inorder_aux(aux.getRight())

    def inorder(self):
        self.inorder_aux(self.node)

    def EncontrarAux(self, a, dato):
        if a == None:
            return None
        else:
            if dato == a.getNombre() or dato == a.getApellido() or dato == a.getCelular() or dato == a.getCorreo():
                return True
            else:
                self.EncontrarAux(a.left,dato)
                self.EncontrarAux(a.right,dato)

    def buscar(self,dato):
        if self.EncontrarAux(self.node,dato):
            return True
        return False

    def AgregarRama(self, a):
        if a is not None:
            self.AgregarRama(a.getLeft())
            self.insertar(a.getNombre(),a.getApellido(),a.getCelular(),a.getCorreo())
            self.AgregarRama(a.getRight())

    def BorrarAux(self, a, dato, cadena):
        if a == None:
            return None
        else:
            self.BorrarAux(a.getRight(),dato,cadena)
            cadena.agregar(a.getNombre(),a.getApellido(),a.getCelular(),a.getCorreo())
            self.BorrarAux(a.getLeft(),dato,cadena)

    def Borrar(self,dato):
        cadena = lista_ordenada()
        self.BorrarAux(self.node, dato, cadena)
        cadena.eliminar(dato)
        self.node = None
        aux = cadena.getHead()
        while aux is not None:
            print aux.getCelular()
            self.insertar(aux.getNombre(),aux.getApellido(),aux.getCelular(),aux.getCorreo())
            aux = aux.getNext()
