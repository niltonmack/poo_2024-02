class Veiculo:
    def __init__(self,marca,modelo,preco_base):
        self.marca = marca
        self.modelo = modelo
        self.preco_base = preco_base
    def calcular_valor_venda(self):
        raise NotImplementedError("Esse método deve ser implementado nas subclasses")
class Carro(Veiculo):
    def __init__(self,marca,modelo,preco_base,num_portas,ac):
        self.num_portas = num_portas
        self.ac = ac
        super().__init__(marca,modelo,preco_base)
    def calcular_valor_venda(self):
        if self.ac:
            valor_ac = 5000
        else:
            valor_ac = 0
        return self.preco_base + valor_ac 
class Moto(Veiculo):
    def __init__(self,marca,modelo,preco_base,cilindradas):
        self.cilindradas = cilindradas
        super().__init__(marca,modelo,preco_base)
    def calcular_valor_venda(self):
        return self.preco_base + self.cilindradas*10
class Caminhao(Veiculo):
    def __init__(self,marca,modelo,preco_base,cap_carga,eixos):
        self.cap_cargas = cap_carga
        self.eixos = eixos
        super().__init__(marca,modelo,preco_base)
    def calcular_valor_venda(self):
        return self.preco_base + self.cap_carga*20 + self.eixos*500
class Concessionaria:
    def __init__(self):
        self.veiculos = []
    def adicionar_veiculo(self):
        pass
    def calcular_valor_estoque(self):
        pass
    def exibir_menu():
        pass
    def incluir_veiculo_menu():
        pass
