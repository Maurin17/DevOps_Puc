class Enemy:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def receber_dano(self, dano):
        dano_real = max(0, dano - self.defesa)
        self.vida -= dano_real
        return dano_real

    def esta_vivo(self):
        return self.vida > 0