nome="Guilherme"
idade=18
profissao="Programador(estagiário)"
linguagem="Python"
dados={"nome":"Guilherme","idade":"18"}
saldo=274.3526

print("Nome: %s. Idade: %d." % (nome, idade))

print("Nome: {}. Idade: {}.".format(nome, idade))
print("Nome: {}. Idade: {}.".format(idade, idade))
print("Nome: {0}. Idade: {1}{1}.".format(nome, idade))
print("Nome: {name}. Idade: {age}{name}{age}{name}.".format(name=nome, age=idade))
print("Nome: {nome}. Idade: {idade}{nome}{idade}{nome}.".format(**dados))

print(f"Nome: {nome}. Idade: {idade}.")
print(f"Nome: {nome}. Idade: {idade}. Saldo: {saldo: .2f}")
print(f"Nome: {nome}. Idade: {idade}. Saldo: {saldo: 10.2f}.")
