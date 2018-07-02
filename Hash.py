#Codigo utilizado en control de clases.

def str2num(apellido):
  return sum([ord(c) for c in apellido])

def hashstr(apellido,size):
    return str2num(apellido)%size

class nodo:
  def __init__(self, nombre, apellido, celular, correo):
      self.nombre = nombre
      self.apellido = apellido
      self.celular = celular
      self.correo = correo

class hash:
  def init(self,size):
    self.lista = [None]*size
    self.size = size
    self.llave = []

  def Insertar (self, nombre, apellido, celular, correo):
    pos = hashstr(apellido,self.size)
    self.llave.append(apellido)
    if self.lista[pos] is not None:
      a = False
      for i in self.list[pos]:
        if i[0] is apellido:
           i[1] = node(nombre, apellido, celular, correo)
           a = True
      if not a:
        self.lista[pos].append(node (nombre, apellido, celular, correo))
    else:
      self.lista[pos] = []
      self.lista[pos].append(apellido, node(nombre, apellido, celular, correo))

  def obtener(self,apellido):
    for i in self.lista[hashstr(apellido,self.size)]:
      if i[0] is apellido:
        return i[1]

  def Borrar(self,apellido):
    pos = hashstr(apellido,self.size)
    if self.lista[pos] is None:
      return False
    else:
      for i in self.lista[pos]:
        if i[0] is apellido:
          i[0] = None
          i[1] = None
  def imprimir (self):
    info = []
    for i in range (0,len(self.llave),+1):
      x = None
      x = get(self.llave[i])
      info.append(x)
    menor = info[0]
    while True:
      for i in range (0,len(info),+1):
        if menor.apellido[0] >= info[i].apellido[0]:
          numero = None
          menor  = info[i]
          numero = i
      print ("Info Contacto:", menor.nombre, menor.apellido, menor.telefono, menor.mail)
      info[numero].remove
      if len(info) == 0:
        False
      
  
