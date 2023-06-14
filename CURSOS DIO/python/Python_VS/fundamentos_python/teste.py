'''
T = input()[0:500]
a=0
for tamanho in T:
  a+=1
if a<=140 and a>0:
  print("TWEET")
else:
  print("MUTE")

  month = int(input())

months_dict = {
    if month==1:
   mes="January"
  elif month==2:
    mes="February"
  elif month==3:
    mes="March"
  elif month==4:
    mes="April"
  elif month==5:
    mes="May"
  elif month==6:
    mes="June"
  elif month==7:
    mes="July"
  elif month==8:
    mes="August"
  elif month==9:
    mes="September"
  elif month==10:
    mes="October"
  elif month==11:
    mes="November"
  elif month==12:
    mes="December"
}
print(mes.title())

month = int(input())

months_dict = {
  1="January"
  2="February"
  3="March"
  4="April"
  5="May""
  6="June"
  7="July"
  8="August"
  9="September"
  10="October"
  11="November"
  12="December"
}
print(mes.title())
'''
month = input()

months_dict = {
  "1":"January",
  "2":"February",
  "3":"March",
  "4":"April",
  "5":"May",
  "6":"June",
  "7":"July",
  "8":"August",
  "9":"September",
  "10":"October",
  "11":"November",
  "12":"December"
}

print(f"{months_dict[month]}")

n = int(input())

for i in range(n):
    a, b = input().split()

    if a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")
'''
Explicação:

Primeiro, lemos a quantidade de casos de teste com a função int(input()).
Em seguida, utilizamos um loop for para iterar sobre cada caso de teste, que serão lidos em pares.
Dentro do loop, utilizamos a função input().split() para ler os valores a e b separadamente, que são as strings a serem comparadas.
Em seguida, verificamos se b é um sufixo de a utilizando o método endswith() das strings. Se for, imprimimos "encaixa", caso contrário, imprimimos "nao encaixa".'''