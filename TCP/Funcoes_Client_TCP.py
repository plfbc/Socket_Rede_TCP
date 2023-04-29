import random
import math

def geracao_n() -> str:
    num_max = math.pow(10, 30) - 1
    numero = random.randint(0, num_max)
    
    return str(numero)
