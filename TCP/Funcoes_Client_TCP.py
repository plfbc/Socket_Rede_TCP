import random

# A função abaixo escolhe qualquer número entre 0 e o maior número de 30 casas decimais.
# Seu funcionamento é dividio em: 1 - Sorteio do número de casas decimais do número 2 - Sorteio do número em sí a partir da potência
# O retorno da função é o número em string.

def geracao_n() -> str:
    pot = random.randint(0,29)
    choice = str(random.randint(10**pot, (10**(pot+1))-1))
    
    return str(choice)
