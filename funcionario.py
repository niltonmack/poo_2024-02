'''
Objetivo: Desenvolver um sistema para gerenciar uma empresa com 
diferentes tipos de funcionários, incluindo salários, cargos e bonificações.
Parte 1: Definir Classes
1. Classe Funcionário: 
- Atributos: nome, ID, salário.
- Métodos: mostrar_detalhes, calcular_bonificacao.
2. Classe Gerente (herda de Funcionário):
3. Classe Engenheiro (herda de Funcionário):
- Atributo adicionais: especialidade (por exemplo, software, hardware).
- Método  mostrar_detalhes (sobrescrito)
'''
class Funcionario:
    def __init__(self,nome, id, salario):
        self.nome = nome
        self.id = id
        self.salario = salario
    def mostar_detalhes(self):
        print(f"nome:{self.nome} id:{self.id} salario:{self.salario}")
    def get_nome(self):
        return self.nome
    def set_nome(self,nome):
        self.nome = nome
    def calcular_bonificacao(self):
        return self.salario*12*0.6
class Gerente(Funcionario):
    def __init__(self, nome, id, salario):
        super().__init__(nome,id,salario)
    def calcular_bonificacao(self):
        return self.salario*12*0.8
class Engenheiro(Funcionario):
    def __init__(self, nome, id, salario, especialidade):
        self.especialidade = especialidade
        super().__init__(nome,id,salario)
    def mostar_detalhes(self):
        print(f"nome:{self.nome} id:{self.id} salario:{self.salario} espe:{self.especialidade}")

func1 = Funcionario("João",1,5000.0)
func2 = Funcionario("Maria",2,7000.0)
gerente = Gerente("Pedro",3,20000)
engenheiro = Engenheiro("Sofia",4,15000,"Eng.Software")

bonus_func1 = func1.calcular_bonificacao()
print(bonus_func1)
print(func1.get_nome())
gerente.set_nome("Pedro Manuel")
print(gerente.get_nome())
bonus_gerente = gerente.calcular_bonificacao()
print(bonus_gerente)
