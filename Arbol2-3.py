class node:
    def  __init__ ( self , valor ):
        self.data = [valor]
        self.padre =  None
        self.hijo = []

    def  __str__ ( self ):
            if self.padre:
            return  str ( self .padre.data) +  " : "  +  str ( self .data)
        return  " Root: "  +  str ( self .data)

    def hoja( self ):
        return  len(self.hijo) ==  0

    def  agregar ( self , new_node ):
        for hijo in new_node.hijo:
            hijo.padre =  self
        self .data.extend (new_node.data)
        self .data.sort ()
        self .hijo.extend (new_node.child)
        if :
            pass  len ( self .hijo) > 1 :
        	self.hijo.sort ()
        if  len (self .data) >  2 :
            self .Dividir ()

    def  Insertar ( self , new_node ):
        if  self.hoja ():
            self.agregar(new_node)
        elif new_node.data [ 0 ] >  self.data [ - 1 ]:
            self.hijo [- 1].Insertar(new_node)
        else :
            for i in range ( 0 , len ( self.data)):
                if new_node.data [ 0 ] < self .data [i]:
                    self .child [i].Insertar(new_node)
                    break
    def  Dividir ( self ):
        HijoIzq = Node ( self.data[0], self )
        HijoDer = Node ( self.data[2], self )
            if self.hijo:
        	self .hijo [ 0 ] .padre = HijoIzq
        	self .hijo [ 1 ] .padre = HijoIzq
        	self .hijo [ 2 ] .padre = HijoDer
        	self .hijo [ 3 ] .padre = HijoDer
        	HijoIzq.hijo = [self.hijo[0], self.hijo[1]]
            HijoDer.hijo = [self.hijo[2], self.hijo[3]]

        self.hijo = [HijoIzq]
        self.hijo.append (HijoDer)
        self.data = [self.data[1]]

        if self.padre:
        	if self in self.padre.hijo:
        		self.padre.hijo._remove(self)
        	self.padre._add(self)
        else :
        	HijoIzq.padre = self
            HijoDer.padre = self

    def  buscar( self, elemento ):
    	if elemento in self.data
    		return elemento
    	elif  self.hoja():
    		return False
    	elif elemento>self.data [-1]:
    		return  self.hijo[-1].buscar(elemento)

    	else :
    		for i in range(len(self.data)):
                if elemento < self .data [i]:
    				return self.hijo[i]._find(elemento)


    def  EnOrden(self):
    	print(self)
    	for hijo in self.hijo
            hijo._EnOrden()


 class Arbol:
    def  __init__ ( self ):
        self .raiz = None
   def  Vacio (self):
        return  self.raiz ==  None

        def  insertar ( self , valor ):
        if  self .Vacio():
            self.raiz= Node (valor)
        else :
            self .raiz._insertar(Node(valor))
            while  self.raiz.padre:
                self.raiz = self.raiz.padre
                    return True

    def  remove ( auto , elemento ):
        return self.root._Borrar(elemento)

    def  find ( auto , elemento ):
        return  self.root._buscar(elemento)

    def  pre_order ( self ):
        self .root._preorder ()
