import random as rd

sorteio = rd.sample(["SIMPLES", "MÉDIO", "RARO"], counts=[6, 3, 1], k=10)
sorteio.sort()
print(sorteio)