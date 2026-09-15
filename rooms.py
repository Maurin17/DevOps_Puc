class Room:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.inimigos = []

    def adicionar_inimigo(self, inimigo):
        self.inimigos.append(inimigo)

    def quantidade_inimigos(self):
        return len(self.inimigos)