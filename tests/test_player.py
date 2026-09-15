from player import Player
from enemy import Enemy
from items import Pocao
from rooms import Room


def test_criar_jogador():
    jogador = Player("Aragorn")

    assert jogador.nome == "Aragorn"
    assert jogador.vida == 30
    assert jogador.ataque == 5
    assert jogador.defesa == 2


def test_jogador_recebe_dano():
    jogador = Player("Aragorn")

    dano = jogador.receber_dano(10)

    assert dano == 8
    assert jogador.vida == 22


def test_jogador_ataca_inimigo():
    jogador = Player("Aragorn")
    inimigo = Enemy("Goblin", 20, 4, 1)

    dano = jogador.atacar(inimigo)

    assert dano == 4
    assert inimigo.vida == 16


def test_pocao_recupera_vida():
    jogador = Player("Aragorn")
    jogador.vida = 10

    pocao = Pocao("Poção de Cura", 10, 15)
    pocao.usar(jogador)

    assert jogador.vida == 25


def test_adicionar_inimigo_na_sala():
    sala = Room("Sala Escura", "Uma sala escura e perigosa.")
    inimigo = Enemy("Goblin", 20, 4, 1)

    sala.adicionar_inimigo(inimigo)

    assert sala.quantidade_inimigos() == 1
    assert sala.inimigos[0].nome == "Goblin"