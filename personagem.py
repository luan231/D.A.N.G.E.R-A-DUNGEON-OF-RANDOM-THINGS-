from random import randint as rd
import json
def criar(nome):
  personagem = {
    nome:{
    "HP": rd(10,50), #vida
    "FOR": rd(0,50), #força
    "DES": rd(0,50), #destreza
    "MAG": rd(0,50), #magia
    "SOR": rd(0,50), #sorte
    "INI": rd(0,50), #iniciativa
    "VON": rd(0,50)  #vontade
    }
  }
  #Esse aqui escrevee
  with open("personagem.json", "w",encoding='utf8') as json_file:
    file = json.dump(personagem, json_file, ensure_ascii=False, indent=4)


  print("\nSuas informações: "
        +str(json.dumps(personagem,ensure_ascii=False,indent=4)))

def habilidades():
  guerreiro = {
    "ataque corpo a corpo": rd(2,4)
  }
  mago = {
    "bola de fogo": rd(2,4)
  }
