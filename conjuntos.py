def union_conjuntos(conjunto_a,conjunto_b):
  print("\nLa union de A y B es {}\n".format(conjunto_a.union(conjunto_b)))

def interseccion_conjuntos(conjunto_a, conjunto_b):
  print("\nLa interseccion de A y B es {}\n".format(conjunto_a.intersection(conjunto_b)))

def diferencia_simetrica_conjuntos(conjunto_a, conjunto_b):
  print("\nLa diferencia simetrica de A y B es {}\n".format(conjunto_a.symetric_difference(conjunto_b)))

def diferencia_conjuntos(conjunto_a, conjunto_b):
  print("Elije la diferencia que quieras realizar:")
  print("1. A - B")
  print("2. B - A")
  operacion = int(input(": "))
  if operacion == 1:
    print("\nLa diferencia de A y B es {}\n".format(conjunto_a.difference(conjunto_b)))
  elif operacion == 2:
    print("\nLa diferencia de B y A es {}\n".format(conjunto_b.difference(conjunto_a)))
  else:
    print("No reconozco esa operacion intenta de nuevo")
    diferencia_conjuntos(conjunto_a,conjunto_b)

def ver_instrucciones():
  print("Operaciones que puedes realizar:")
  print("1 Union")
  print("2 Interseccion")
  print("3 Diferencia")
  print("4 Diferencia Simetrica")
  print("5 Ver instrucciones")
  print("6 Salir")


def calculadora_conjuntos():
  print("Bienvenido a los conjuntos")
  print("Introduce los elementos de los conjuntos separados por espacios")
  print("Ejemplo: 1 3 4 8 0 2") 

  conjunto_a = set(input("Conjunto A: ").split())
  conjunto_b = set(input("Conjunto B: ").split())

  ver_instrucciones()
  while True:
    	
    operacion = int(input(": "))
    if operacion == 1:
      union_conjuntos(conjunto_a,conjunto_b) 	
    elif operacion == 2: 
      interseccion_conjuntos(conjunto_a,conjunto_b)    
    elif operacion == 3: 
      diferencia_conjuntos(conjunto_a,conjunto_b)
    elif operacion == 4: 
      diferencia_simetrica_conjuntos(conjunto_a,conjunto_b)
    elif operacion == 5: 
      ver_instrucciones()
    elif operacion == 6: 
      break
    else:
      print("No reconozco esa operacion. Intenta de nuevo")

calculadora_conjuntos()






