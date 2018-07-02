class ArbolAVL():
    def __init__(self, *args):
        self.node = None
        self.altura = -1
        self.balance = 0;

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def Altura(self):
        if self.node:
            return self.node.altura
        else:
            return 0

    def Hoja(self):
        return (self.altura == 0)

    def insertar(self, nombre, apellido, celular, correo):
        arbol = self.node
        newnode = Node(nombre, apellido, celular, correo)

        if arbol == None:
            self.node = newnode
            self.node.izq = ArbolAVL()
            self.node.der = ArbolAVL()


        elif apellido < arbol.getApellido():
            self.node.izq.insertar(nombre, apellido, celular, correo)

        elif apellido > arbol.getApellido():
            self.node.der.insertar(nombre, apellido, celular, correo)

        else:
            self.node.izq.insertar(nombre, apellido, celular, correo)
        self.rebalance()

    def RotacionIzq(self):

        A = self.node
        B = self.node.der.node
        C = B.izq.node

        self.node = B
        B.izq.node = A
        A.der.node = C

    def RotacionDer(self):

        A = self.node
        B = self.node.izq.node
        C = B.der.node

        self.node = B
        B.der.node = A
        A.izq.node = C


    def rebalance(self):

        self.Act_altura(False)
        self.Act_balance(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.izq.balance < 0:
                    self.node.izq.RotacionIzq()
                    self.Act_altura()
                    self.Act_balance()
                self.RotacionDer()
                self.Act_altura()
                self.Act_balance()

            if self.balance < -1:
                if self.node.der.balance > 0:
                    self.node.der.RotacionDer()
                    self.Act_altura()
                    self.Act_balance()
                self.RotacionIzq()
                self.Act_altura()
                self.Act_balance()


    def Anterior(self, node):
        node = node.left.node
        if node is not None:
            while node.der is not None:
                if node.der.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def siguiente(self, node):
        node = node.der.node
        if node is not None:
            while node.izq is not None:
                if node.izq.node == None:
                    return node
                else:
                    node = node.izq.node
        return node

    def Act_altura(self, b=True):
        if not self.node == None:
            if b:
                if self.node.izq != None:
                    self.node.izq.Act_altura()
                if self.node.der != None:
                    self.node.der.Act_altura()

            self.altura = max(self.node.izq.altura,
                              self.node.der.altura) + 1
        else:
            self.altura = -1

    def Act_balance(self, b=True):
        if not self.node == None:
            if b:
                if self.node.izq != None:
                    self.node.izq.Act_balance()
                if self.node.der != None:
                    self.node.der.Act_balance()

            self.balance = self.node.izq.altura - self.node.der.altura
        else:
            self.balance = 0

    def buscar(self,info):                                                          #BUSCAR
        if(self.node is not None):
            if self.node.llave == info:
                print(True)
                return True
            self.node.izq.buscar(info)
            self.node.der.buscar(info)
        return


    def Borrar(self, key):
        if self.node is not None:
            if self.node.getApellido() == llave:

                if self.node.izq.node == None and self.node.der.node == None:
                    self.node = None

                elif self.node.izq.node == None:
                     self.node = self.node.der.node

                elif self.node.der.node == None:
                    self.node = self.node.izq.node


                else:
                    reemplazar = self.siguiente(self.node)
                    if reemplazar is not None:
                        self.node.setApellido(reemplazar.key)
                        self.node.right.Borrar(reemplazar.key)

                self.rebalance()
                return
            elif info < self.node.getApellido():
                self.node.izq.Borrar()

            elif info > self.node.getApellido():
                self.node.der.Borrar(info)

            self.rebalance()
        else:
            return

    def RevisarBalance(self):
        if self == None or self.node == None:
            return True
        self.Act_altura()
        self.Act_balance()
        return ((abs(self.balance) < 2) and self.node.izq.RevisarBalance() and self.node.der.RevisarBalance())

    def imprimir(self):                                                            #IMPRIMIR
        self.Act_altura()
        self.Act_balance()
        if(self.node is not None):
            self.node.izq.imprimir()
            print (self.node.getApellido())
            self.node.der.imprimir()
