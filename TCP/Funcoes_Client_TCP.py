import random
import math

def geracao_n() -> str:
    pot = random.randint(0,29)
    choice = str(random.randint(10**pot, (10**(pot+1))-1))
    
    return str(choice)
