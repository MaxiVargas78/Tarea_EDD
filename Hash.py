def str2num(key):
  return sum([ord(c) for c in key])

def hashstr(key,size):
  return str2num(key)%size


class Libro:
    def __init__(self, titulo, autor, ventas, nota, especialidad, comentarios):
        self.titulo = titulo
        self.autor = autor
        self.ventas = ventas
        self.nota = nota
        self.especialidad = especialidad
        self.comentarios = comentarios

        def crear(self, new node):


class hash:
  def __init__(self,size):
    self.list = [None]*size
    self.size= size
  
  def put(self,key,val):
    pos = hashstr(key,self.size)
    if self.list[pos] is not None:
      print("collision "+key+"<br>")
      ok = False
      for t in self.list[pos]:
        if t[0] is key:
          t[1] = val
          ok = True
      if not ok:
        self.list[pos].append([key,val])
    else:
      self.list[pos] =[]
      self.list[pos].append([key,val])
    
  def get(self,key):
    for e in self.list[hashstr(key,self.size)]:
      if e[0] is key:
        return e[1]



      
  
