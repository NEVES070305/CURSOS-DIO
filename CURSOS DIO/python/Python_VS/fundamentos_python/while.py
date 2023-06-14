opcao =- 1
while opcao != 0:
    opcao = int(input("Escolha sacar(1) ou depositar(2): "))

    if opcao == 1:
        print("Você escolheu sacar.")
        opcao_saque=-1
        while opcao_saque != 0 and opcao_saque!=1 and opcao_saque!=2:
           opcao_saque  =int(input("Escolha 1: para notas menores e 2: para notas maiores."))

           if opcao_saque == 1:
             print("Escolheu sacar notas menores.")
           elif opcao_saque==2:
                print("Escolheu sacar notas maiores.")
           else:
                print("Receberá aleatoriamente.")
    elif opcao==2:
        print("Você escolheu depositar: ")
        deposito=int(input("Qual o valor deseja depositar?"))
        print(f"Você escolheu depositar {deposito}. Até mais")
    else:
       print("Você não escolheu nenhuma das opções disponíveis.")
       print("Escolha novamente.")
else:
    print("Obrigado por estar no nosso banco digital.")