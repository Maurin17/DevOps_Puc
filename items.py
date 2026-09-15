class Item:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class Pocao(Item):
    def __init__(self, nome, valor, cura):
        super().__init__(nome, valor)
        self.cura = cura

    def usar(self, jogador):
        jogador.vida += self.cura