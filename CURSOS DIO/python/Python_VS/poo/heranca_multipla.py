class Animal:
    def __init__(self,numero_patas):
        self.numero_patas=numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
     def __init__(self,cor_pelo,**kw):
        super().__init__(**kw)
        self.cor_pelo=cor_pelo

class Ave(Animal):
     def __init__(self,cor_bico,**kw):
        super().__init__(**kw)
        self.cor_bico=cor_bico

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero,Ave): #Herança múltipla

    def __init__(self, cor_pelo, cor_bico, numero_patas):
        print(Ornitorrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo,cor_bico=cor_bico,numero_patas=numero_patas)

animal=Animal(numero_patas=2)
print(animal)
#gato=Gato("Dourado",4)
#print(gato)

ornitorrinco=Ornitorrinco(numero_patas=3,cor_pelo="Verde",cor_bico="Laranja")
print(ornitorrinco)

ornitorrinco_2=Ornitorrinco("Azul","Avermelhado",3)
print(ornitorrinco_2)