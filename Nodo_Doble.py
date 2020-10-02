class NodoDoble:
   def __init__(self, value, siguiente = None, previo = None):
      self.data = value
      self.next = siguiente
      self.prev = previo

class ListaDobleLigada:
   def __init__ (self):
      self.__head = None
      self.__tail = None

   def is_empty(self):
         return self.__head == None
      
   def append(self, value):
      #Vacío
      if self.is_empty( ):
         self.__head = NodoDoble(value)
         self.__tail =  self.__head
      else:
         nuevo = NodoDoble(value)
         self.__tail.next = nuevo
         nuevo.prev = self.__tail
         self.__tail = nuevo

         """
         self.__tail.next = NodoDoble(value, None, self.__tail)
         self.__tail = self.tail.next
         """
   def transversal(self):
      nodo_actual = self.__head
      while nodo_actual.next != None:
                     print(f"{nodo_actual.data}--->", end = "")
                     nodo_actual = nodo_actual.next
      print(nodo_actual.data)

   def reverse_transversal(self):
      nodo_actual = self.__tail
      while nodo_actual.prev!= None:
         print(f"{nodo_actual.data}--->", end = "")
         nodo_actual = nodo_actual.prev
      print(nodo_actual.data)

   
   def get_size(self):
      nodo_actual = self.__head
      contador = 1
      while nodo_actual.next != None:
         nodo_actual = nodo_actual.next
         contador += 1
      return contador

   def find_from_head(self,value):
      nodo_actual = self.__head
      #encontrado = None
      while nodo_actual != value:
         if nodo_actual.next == None:
            return None
         nodo_actual = nodo_actual.next
      #if nodo_actual.data == value:
         #encontrado = nodo_actual
      return nodo_actual

   def insert_from_head(self,reference_value,value):
      nodo = self.find_from_head(reference_value)
      if nodo != None:
         nuevo  = NodoDoble(value, nodo.next,nodo)
         nodo.next = nuevo
         if nuevo.next != None:
            nodo.next.prev = nuevo
       

