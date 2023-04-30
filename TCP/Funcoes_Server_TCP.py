import random
import string as st

# A função abaixo fornece a resposta final do servidor ao cliente
# Seu fluxo é dado pela verificação do número de casas decimais do argumento recebido e a consequente formulação da resposta.

def server_resp(str_cli:str) -> str:

    caracteres = st.ascii_letters + st.digits + st.punctuation

    if (len(str_cli) > 10):
        str_resp = ''.join(random.choices(caracteres, k=len(str_cli)))
        
    else:
        num_cli = int(str_cli)

        if (num_cli % 2 == 0):
            str_resp = 'Número enviado pelo cliente é par'
        
        else:
             str_resp = 'Número enviado pelo cliente é ímpar'

    return str_resp
