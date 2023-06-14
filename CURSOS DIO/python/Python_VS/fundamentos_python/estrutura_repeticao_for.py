texto=input("Informe seu texto: ")
VOCAIS="AEIOU"

#Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOCAIS:
        print(letra,end="")
else:
    #executa no final do laço
    print()
    print("Executa no final do laço.")

#Exemplo com range
for numero in range(0,10):
    print(numero, end="")

for numero in range(0,51,5):
    print(numero, end=" ")