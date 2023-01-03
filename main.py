import personagem
from time import sleep as delay

print('\033[92m'+" ______   _______  _        _______  _______  _______  _ \n"+
      "(  __  \ (  ___  )( (    /|(  ____ \(  ____ \(  ____ )( )\n"+
     "| (  \  )| (   ) ||  \  ( || (    \/| (    \/| (    )|| |\n"+
     "| |   ) || (___) ||   \ | || |      | (__    | (____)|| |\n"+
     "| |   | ||  ___  || (\ \) || | ____ |  __)   |     __)| |\n"+
     "| |   ) || (   ) || | \   || | \_  )| (      | (\ (   (_)\n"+
     "| (__/  )| )   ( || )  \  || (___) || (____/\| ) \ \__ _ \n"+
     "(______/ |/     \||/    )_)(_______)(_______/|/   \__/(_)\n"+
     "UMA MASMORRA DE COISAS ALEATÓRIAS!")
delay(2)
nome_personagem = input("Digite um nome para seu personagem: ")
personagem.criar(nome_personagem)


#Primeiro de tudo: lista de atributos
#vida(10/50), força(0/50), destreza(0,50), magia(0,50), sorte(0,50), iniciativa(0,50), vontade(0,50)

#Terceiro: personagem e as listas de ataques
#luta corpo a corpo, ataque à distância, esquiva, bloqueio, contra ataque, bola de fogo, relâmpago, congelamento, areia movediça, soco de fogo, bola de agua cristalizada, terra espinhenta, ventos cortantes, flechas congelantes, 

#Quarto: inimigos
#slime(HP:2/ATK:1), goblin(HP:5/ATK:2), rato(HP:3/ATK:1/pode matar por envenamento), abelha(HP:1/ATK:1/pode matar por envenenamento), esqueleto(HP:10/ATK:5), zumbi(HP:12/ATK:5), aranha gigante(HP:20/ATK:15/pode matar por envenenamento), arvore mutante (HP:50/ATK:10), guarda zumbi (HP:25/ATK:15).
#Bosses: Rei Slime(HP:10/ATK:5), Esqueleto Gigante(HP:20/ATK:10), Aranha Rainha(HP:50/ATK:25), Demônio(HP:100/ATK:100/ultrararo e permite o jogador subir até o nível 10 caso vença)

#Quinto: tempo limite até o combate
#Até o personagem chegar no nível 5, cada nível ele ganha 2 pontos para distribuir onde ele quiser, sendo 50 o valor máximo.

#Sexto: o combate
#O jogador pode escolher os ataques e quando subir de nível escolher onde distribuir os pontos, ao chegar no nível 5 o personagem será congelado e não poderá mais evoluir, mas ele ainda pode morrer em combate.
