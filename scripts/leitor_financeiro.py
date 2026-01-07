import pandas as pd

df = pd.read_excel("../dados/controle_financeiro.xlsx")

total_entrada = df["ENTRADA"].sum()
total_saida = df["SAIDA"].sum()
saldo = total_entrada - total_saida

print("Total de Entradas:", total_entrada)
print("Total de Saídas:", total_saida)
print("Saldo:", saldo)
