
import random

from .personagem import *

class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade

  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

  def ataque_especial(self, alvo):
    dano = random.randint(self.get_nivel() * 6,self.get_nivel() * 8) # Dano aumentado
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
