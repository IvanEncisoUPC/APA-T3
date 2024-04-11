
# Definimos la función __mul__:

def __mul__(self, other):
        
    # Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

    if isinstance(other, Vector):
        return Vector([a * b for a, b in zip(self, other)])
    elif isinstance(other, (int, float, complex)):
        return Vector([other * x for x in self])

__rmul__ = __mul__

# Definimos la función __matmul__:

def __matmul__(self, other):
        
     # Método para implementar el producto escalar de dos vectores.
        
     return sum([a * b for a, b in zip(self, other)])
        
__rmatmul__ = __matmul__

# Definimos la función __floordiv__

def __floordiv__(self, other):
        
     # Método para que devuelva la componente tangencial.
           
     return Vector([(sum(a * b for a, b in zip(self, other)) // (sum(a ** 2 for a in other) ** 0.5)) * b for b in other])

__rfloordiv__ = __floordiv__

# Definimos la función __mod__:

def __mod__(self, other):
        
      # Método para que devuelva la componente normal o perpendicular.
        
      return self - self // other
    
__rmod__ = __mod__
