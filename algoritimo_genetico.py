class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor

if __name__ == '__main__':
    p1 = Produto("Iphone 6", 0.0000899, 2199.12)
    
print(p1.nome)