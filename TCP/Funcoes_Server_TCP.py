import random
import string as st


def server_resp(str_cli:str) -> str:

    caracteres = st.ascii_letters + st.digits + st.punctuation

    if (len(str_cli) > 10):
        str_resp = ''.join(random.choices(caracteres) for i in range(len(str_cli)))
        
    else:
        num_cli = int(str_cli)

        if (num_cli % 2 == 0):
            str_resp = 'Número enviado pelo cliente é par'
        
        else:
             str_resp = 'Número enviado pelo cliente é ímpar'

    return str_resp