import matplotlib.pyplot as plt
maior=df_nomes_aparicoes["aparicoes"].idxmax()
print(df_nomes_aparicoes.loc[maior])
print(maior)
df_nomes_aparicoes.plot()