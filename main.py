import sys


def termometro(temp:float):
  if(temp <=15):
    return("Frio")
  elif(temp >=27):
    return("Quente")
  else:
    return("Agradável")
# Classe B
assert termometro(14)== "Frio"
assert termometro(15)== "Frio"
assert termometro(16)== "Frio"
assert termometro(26)== "Quente"
assert termometro(27)== "Quente"
assert termometro(28)== "Quente"
# Classe C
assert termometro(sys.float_info.max -1)== "Quente"
assert termometro(sys.float_info.max)== "Quente"
assert termometro(sys.float_info.max +1)== "Quente"
#Classe A 
assert termometro(sys.float_info.min -1) == "Frio"
assert termometro(sys.float_info.min) == "Frio"
assert termometro(sys.float_info.min +1) == "Frio"