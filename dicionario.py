import json
#estrutura de dados
dic = {}
dic = {"nome":"João",
       "profissão":"Engenheiro",
       "cpf":"0950000000",
       "endereço":{"rua":"Pedro",
                   "cep":"02333333"}
        }

valor = dic.get("nome1","chave não encontra")
print(valor)
dic['sobrenome'] = "furtado"
valor = dic.get("sobrenome","chave não encontra")
print(valor)
cep = dic['endereço']['cep']
print(cep)
#del dic['profissão']
for v in dic.values():
    print(v)
for v in dic.keys():
    print(v)
for k,v in dic.items():
    print(k,v)

for v in dic.values():
    if isinstance(v,dict):
        for k1,v1 in v.items():
            print(k1,v1)