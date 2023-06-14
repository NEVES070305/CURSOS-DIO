valor=input("Insira quanto quer sacar: ")
def sacar(valor):
    saldo=500
    if saldo>=valor:
        print("Valor sacado!")
        print("Retire sue dinheiro no caixa")
    else:
        print("Você não tem saldo suficiente",end=". \n")
        print(f"Seu saldo é {saldo}.")
    print("Obrigado por ser nosso cliente!")

def depositar(valor):
    saldo=500
    saldo+=valor

sacar(float(valor))