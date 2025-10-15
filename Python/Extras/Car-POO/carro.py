# instancia: é a criação de um objeto a partir de uma classe
# objeto: é a instancia de uma classe

# minhas dúvidas:
# diferença entre atributos de classe, atributos de instancia e atributos privados
# diferença entre métodos de classe, métodos de instancia e métodos estáticos
# diferença entre métodos e funções
# diferença entre self e cls

class Carro: # "class" em minuscolo. Classe é um "molde", que define métodos e atributos
    
    # ---------------------
    # ATRIBUTOS (de classe)
    # ---------------------
    rodas = 4
    tipo = "Terreste"
    
    # --------
    # MÉTODOS
    # --------
    
    # construtor - chamado automaticamente quando classe é instanciada
    # atibutos de instancia: atributos que pertencem a instancia, definidas no construtor
    # diferença: atributos de classe são compartilhados entre todas as instancias 
    # todos tem 4 rodas e são terrestres, mas nem todos tem marca e cor igual

    def __init__(self, marca, modelo, cor, velocidade_maxima, placa): # self = referencia ao objeto instanciado
        
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.placa = placa
        
        self.velocidade_atual = 0 # atributo de instancia, inicializado com valor padrão
        # não está no enuncidao pois é um atributo que varia com o tempo
        
        self.__ligado = False # atributo privado (não pode ser acessado fora da classe). PRIVADO
        
    def ligar(self):
        if self.__ligado:
            print(f"O carro {self.modelo} de placa {self.placa} já está ligado.")
        else:
            self.__ligado = True
            print(f"O carro {self.modelo} de placa {self.placa}foi ligado.")
            
    def acelerar(self, incremento): # incremento em km/h
        if self.__ligado:
            self.velocidade_atual += incremento
            if self.velocidade_atual >= self.velocidade_maxima:
                self.velocidade_atual = self.velocidade_maxima
                print("Velocidade máxima atingida.")
            print(f"O carro acelerou para {self.velocidade_atual} km/h.")
        else:
            print(f"O carro está desligado.")
        
    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            self.velocidade_atual = 0
            print(f"O carro {self.modelo} de placa {self.placa}foi desligado.")
        else:
            print(f"O carro {self.modelo} de placa {self.placa} já está desligado.")
            
    # ------------------------------------------------------------------------------------   
    # ENCAPSULAMENTO - acesso controlado aos atributos privados (no caso, self.__ligado)
    # ------------------------------------------------------------------------------------
    
    # getter - método para obter o valor de um atributo privado
    def esta_ligado(self):
        return self.__ligado
    
    # setter - modificar. No caso, feito via métodos ligar() e desligar()
        # def set_ligado(self, valor_boleano):
        #     self.__ligado = valor_boleano
    
    # ------------------------------------------------------
    # POLIMORFISMO - mesmo método, comportamentos diferentes
    # ------------------------------------------------------
    
    def __str__(self): # altera como o objeto é representado como string
        return (
            f"Carro {self.marca}, "
            f"Modelo {self.modelo}, "
            f"Cor: {self.cor}, "
            f"Placa: {self.placa}, "
            f"Velocidade Atual: {self.velocidade_atual} km/h, "
            f"Velocidade Máxima: {self.velocidade_maxima} km/h"
        )
        
# ---------------------
# OBJETOS / INSTANCIAS 
# ---------------------

# em ordem do self: marca, modelo, cor, velocidade_maxima, placa
meu_carro = Carro(
    "Toyota",
    "Corolla",
    "Prata",
    180,
    "ABC-1234"
    )

print("--------------- Testes ---------------")

print(meu_carro) # usa o método __str__

carro_do_vizinho = Carro(
    "Honda",
    "Civic",
    "Preto",
    200,
    "XYZ-5678"
    )

# -----------------------
# TESTANDO OS ATRIBUTOS
# -----------------------
print(carro_do_vizinho) # usa o método __str__
print(f"\nMeu carro é um {meu_carro.modelo}, e o do vizinho é um {carro_do_vizinho.modelo}.") # atributo de classe
print(f"A cor do carro do meu vizinho é {carro_do_vizinho.cor}")

# -----------------------
# TESTANDO OS MÉTODOS
# -----------------------

meu_carro.acelerar(20) # carro desligado
meu_carro.ligar() # liga o carro
meu_carro.acelerar(50) # acelera
meu_carro.acelerar(150) # tenta acelerar além da velocidade máxima
print(f"Meu carro está ligado? {meu_carro.esta_ligado()}")
meu_carro.desligar()
print(f"Meu carro está ligado? {meu_carro.esta_ligado()}\n")
meu_carro.desligar() # tenta desligar novamente
