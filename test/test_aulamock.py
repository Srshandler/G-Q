import src.aulamock


def test_chave(mocker):
  mocker.patch.object(
    src.aulamock,
    "VALOR_CHAVE",
    "17147oisjiodio"
  )


  assert src.aulamock.VALOR_CHAVE == "17147oisjiodio"

# mock de funcoes
def test_soma(moker):


  moker.patch(
    'src.aulamock.soma',
    return_value= 500
  )
  assert src.aulamock.soma(10,20) == 30

#mock metodos de classes 
def test_mock_metodo(mocker):
  
  def get_nome_fake(self):
    return "Joao"
    
  mocker.patch(
  'src.aulamock.Pessoas.get_nome',
  get_nome_fake
)
  p = src.aulamock.Pessoas("Nome Qualquer")
  assert p.get_nome() == "Ambrosia"