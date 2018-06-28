nodo de clase :
    def  __init__ ( self , valor ):
        self .data = [valor]
        self .parent =  Ninguno
        self .child = []

    def  __str__ ( self ):
        si es  auto .parente:
            return  str ( self .parent.data) +  " : "  +  str ( self .data)
        return  " Root: "  +  str ( self .data)

    def  _is_leaf ( self ):
        return  len ( self .child) ==  0

    def  _add ( self , new_node ):
        para niño en new_node.child:
            child.parent =  self
        self .data.extend (new_node.data)
        self .data.sort ()
        self .child.extend (new_node.child)
        si  len ( self .child) >  1 :
        	self .child.sort ()
        si  len ( self .data) >  2 :
            self ._split ()

    # Encuentra el nodo correcto donde insertar el nuevo nodo
    def  _insert ( self , new_node ):

        # Si es hoja, añade el dato a la hoja y hace un balanceo
        if  self ._is_leaf ():
            self ._add (new_node)

        # Si no es hoja, debe encontrar el hijo correcto para descender y hace una inserción recursiva
        elif new_node.data [ 0 ] >  self .data [ - 1 ]:
            self .child [ - 1 ] ._ insert (new_node)
        else :
            para mí en el  rango ( 0 , len ( self .data)):
                if new_node.data [ 0 ] <  self .data [i]:
                    self .child [i] ._ insert (new_node)
                    descanso

    # Cuando hay 3 elementos en el nodo, se divide en un nuevo sub-arbol y se agrega al padre
    def  _split ( self ):
        left_child = Node ( self .data [ 0 ], self )
        right_child = Node ( self .data [ 2 ], self )
        si  yo mismo .child:
        	self .child [ 0 ] .parent = left_child
        	self .child [ 1 ] .parent = left_child
        	self .child [ 2 ] .parent = right_child
        	self .child [ 3 ] .parent = right_child
        	left_child.child = [ self .child [ 0 ], self .child [ 1 ]]
        	right_child.child = [ self .child [ 2 ], self .child [ 3 ]]

        self .child = [left_child]
        self .child.append (right_child)
        self .data = [ self .data [ 1 ]]

        # Ahora tenemos un nuevo sub-árbol, y necesitamos agregarlo a su nodo padre
        si es  auto .parente:
        	Si  auto  en  auto .parent.child:
        		auto .parent.child.remove ( auto )
        	self .parent._add ( self )
        else :
        	left_child.parent =  self
        	right_child.parent =  self

	# Busca un elemento en el árbol y lo retorna al otro lado, en caso contrario retorna Falso
    def  _find ( auto , elemento ):
    	si el elemento en  sí mismo .data:
    		artículo devuelto
    	elif  self ._is_leaf ():
    		regresar  False
    	elif item >  self .data [ - 1 ]:
    		return  self .child [ - 1 ] ._ find (item)
    	else :
    		para mí en  rango ( len ( self .data)):
    			if item <  self .data [i]:
    				return  self .child [i] ._ find (item)

    def  _remove ( auto , elemento ):
    	pasar

	# Imprime en preordenar
    def  _preorder ( self ):
    	imprimir ( auto )
    	para niño en  sí mismo .child:
            child._preorder ()


 árbol de clase :
    def  __init__ ( self ):
        self .root =  Ninguno

    def  empty ( self ):
        return  self .root ==  Ninguno

    def  insertar ( self , valor ):
        # Cuando se inserta un valor, siempre se crea un nuevo nodo
        if  self .empty ():
            self .root = Node (valor)
        else :
            self .root._insert (Node (valor))
            while  self .root.parent:
                self .root =  self .root.parent
        devolver  verdadero

    def  remove ( auto , elemento ):
        pasar

    def  find ( auto , elemento ):
        return  self .root._find (item)

    def  pre_order ( self ):
        self .root._preorder ()

si  __name__ == " __main__ " :
    pasar
