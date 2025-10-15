from carro import Carro

# --------
# HERANÇA
# --------

class Batmovel(Carro):
    
    modoCombate = True # atributo de classe, todo Batmovel tem modo combate, mas não todo carro
    
    def __init__(self, marca, modelo, cor, velocidade_maxima, placa, modo_aquatico):
        
        super().__init__(marca, modelo, cor, velocidade_maxima, placa) # chama o construtor da classe
        self.modo_aquatico = modo_aquatico  # atributo de instancia, 
                                            # todos os batmoveis tem modo de combate,
                                            # mas não todos tem modo aquático
    # metodo exclusivo
    def ativar_modo_combate(self):
        if self.esta_ligado():
            if self.modoCombate:
                print("Modo combate já está ativado.")
            else:
                self.modoCombate = True
                print("Modo combate ativado.")
        else:
            print("O Batmovel está desligado.")
            
    # sobrescrita de método (override)
    def acelerar(self, incremento): 
        if self.esta_ligado():
            self.velocidade_atual += incremento * 2 # acelera o dobro
        else:
            print(f"O Batmovel está desligado.")
        
tumbler = Batmovel("Wayne", "V1", "Preto", 325, "wyn-1234", True)

print(tumbler) # Usa o __str__ herdado da classe Carro
print(f"O batmovel tem {tumbler.rodas} rodas. (Herança de Atributo de Classe)")

tumbler.ligar() # Método herdado
tumbler.acelerar(50) # Método sobrescrito, sem turbo

tumbler.ativar_modo_combate()
tumbler.acelerar(50) # Método sobrescrito, com bônus de turbo
print(f"Velocidade final do esportivo: {tumbler.velocidade_atual} km/h\n")
