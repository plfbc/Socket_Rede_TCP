import socket
import Funcoes_Client_TCP as FCT
from time import sleep

host = '127.0.0.1'
port = 5000

while True:
    interface_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    interface_s.connect((host,port))
    print('Conexão feita com: {host}:{port}')
#--------------------------------------------------------------------#
# Essa fração do código é responsável por interagir com o servidor, enviando mensagens e recebendo
    msg_cliente = FCT.geracao_n()
    print(f'String original: {msg_cliente}')
    interface_s.sendall(str.encode(msg_cliente))

    data = interface_s.recv(1024)
    print(f'Mensagem do servidor: {data.decode()} \nFIM' )
    
#-------------------------------------------------------------------#
# A fim de criar o tempo entre ciclos de interação, essa fração do código estabelece 10s de espera.
    for i in range(10):
        sleep(1)
        print(f"\nesperando recomeço de ciclo, passou {i+1} segundos")

    
