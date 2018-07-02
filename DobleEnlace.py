class Node:
    def __init__(self, nombre, apellido, celular, correo):
        self.data = data(nombre, apellido, celular, correo)
        self.next_node = None
        self.prev_node = None

class DobleEnlace:
    def __init__(self):
        self.head = None
        self.tail = None

    def Vacio(self):
        return self.head == None

    def InsertarFinal(self, element):
        if self.Vacio():
            self.head = data
            self.tail = self.head
        else:
            data  = data(nombre, apellido, celular, correo)
            self.tail.next_node = data
            node.prev_node = self.tail
            self.tail = data

    def InsertarInicio(self, elemento):
        if self.Vacio():
            self.head = data
            self.tail = self.head
        else:
            data = data(nombre, apellido, celular, correo)
            node.next_node = self.head
            self.head.prev_node = data
            self.head = data

    def Borrar(self,elemento):								#ELIMINA UN CONTACTO POR DATO
		if self.head == None:
			return

		aux = self.head
		prev = aux

		if aux.getapellido() == elemento:
			self.head = aux.getNext()

		while aux is not None:
			if aux.getapellido() == elemento:
				prev.setNext(aux.getNext())
				return
			else:
				prev = aux
				aux = aux.getNext()


    def Imprimir(self):
        if self.Vacio():
             print("Lista vacia")
        else:
            temp = self.head
            i = 1
            while True:
                print("Nodo {} contiene el número {}".format(i, temp.data))
                temp = temp.next_node
                i += 1
                if temp == None:
                    break
