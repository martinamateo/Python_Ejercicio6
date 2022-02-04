

from math import sqrt

def lado_h(lado_a):
   return sqrt(lado_a**2 - (lado_a/2)**2)

def sup_triangulo_rectangulo(lado_a):
   return ((lado_a/2) * lado_h(lado_a))/2

def sup_triangulo_equilatero(lado_a):
 return sup_triangulo_rectangulo(lado_a) * 2
  
def superficie_hexagono(lado_a):
   return sup_triangulo_equilatero(lado_a) * 6

print("Superficie de un hexágono con 6 lados de 17cm: ",superficie_hexagono(17),"Cm2")
print("Superficie de un hexágono con 6 lados de 22cm: ",superficie_hexagono(22),"Cm2")
print("Superficie de un hexágono con 6 lados de 2cm: ",superficie_hexagono(2),"Cm2")
print("Superficie de un hexágono con 6 lados de 4cm: ",superficie_hexagono(4),"Cm2")
