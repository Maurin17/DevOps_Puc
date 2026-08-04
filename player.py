class Player:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 30
        self.ataque = 5
        self.defesa = 2
        self.ouro = 0
        self.nivel = 1

    def mostrar_status(self):
        print("\n===== STATUS =====")
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")
        print(f"Ouro: {self.ouro}")
        print(f"Nível: {self.nivel}")
        print("==================\n")