Class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class ABB:
    def __init__(self, value):
        self.root = None

    def empty(element):
        return self.root == None

    def __add(self, value, node):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
                return
            self.__add(value, node.left)
        elif value > node.value:
            if node.right == None:
                node.right = Node(value)
                return
            self.__add(value, node.right)

    def add(self, value):
        if self.empty():
            node = Node(value)
            self.root = node
        else:
            __add(self, value, self.root)

    def __search(self, value, node):
        if value == node.value:
            return True
        elif value < node.value:
            self.__search(self, value, node.left)
        else:
            self.__search(self, value, node.right)

    def search(self, value):
        if self.empty():
            return False
        else:
            self.__search(self, value, self.root)

    def delete():
    pass

    def pre_order(self, root):
        if root is None:
          pass
        else:
          print(root.data)
          self.pre_order(root.left)
          self.pre_order(root.right)


    def in_order(self, root):
        if root is None:
          pass
        else:
          self.in_order(root.left)
          print(root.data)
          self.in_order(root.right)

    def post_order(self, root):
        if root is None:
          pass
        else:
          self.post_order(root.left)
          self.post_order(root.right)
          print(root.data)





    def leaf_number(self):


    def tree_height(): #Implementar
        pass

    def node_height(): #Implementar
        pass

    def find_minimum(self): #Implementar
      if root is None:
        pass
      else:
        self.in_order(root.left)
          print(root.data)
            return True
    def find_maximum(): #Implementar
        pass
