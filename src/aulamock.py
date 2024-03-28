VALOR_CHAVE ="17147oisjiodio"

def soma (x:int, y:int):
  return x+y

class Pessoas:
  _nome : str
  
  def __init__(self, nome: str):
    self._nome = nome

  def get_nome(self):
    return self._nome 