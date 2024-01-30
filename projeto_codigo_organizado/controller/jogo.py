from model import *

class Jogo:
  """ Classe orquestradora do jogo """

  def __init__(self) -> None:
    self.heroi = Heroi('Gandalf', 100, 10, 'Lança Magica')
    self.inimigo = Inimigo('Ork', 80, 8, 'Monstro')

  def iniciar_batalha(self):
    """ Fazer a gestão da batalha em turnos """
    print("Iniciando batalha!")
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      print("\nDetalhes dos Personagens:")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("Pressione Enter para atacar...")
      escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

      if escolha == '1':
        self.heroi.atacar(self.inimigo)
      elif escolha == '2':
        self.heroi.ataque_especial(self.inimigo)
      else:
        print("Escolha inválida. Escolha novamente.")
      
      if self.inimigo.get_vida() > 0:
        # Inimigo ataca o heroi
        self.inimigo.atacar(self.heroi)

    if self.heroi.get_vida() > 0:
      print("\nParabéns você venceu a batalha!")
    else:
      print("\nVocê foi derrotado!")
