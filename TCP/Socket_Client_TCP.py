import socket
import Funcoes_Client_TCP as FCT
from time import sleep

host = '127.0.0.1'
port = 5000

while True:
    interface_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    interface_s.connect((host,port))
#---------------------------------#

    msg_cliente = FCT.geracao_n()

    interface_s.sendall(str.encode(msg_cliente))

    data = interface_s.recv(1024)
    print('Mensagem do servidor: ', data.decode())
    

    for i in range(10):
        sleep(1)
        print("\nesperando recomeço de ciclo, passou " + [i+1] +" segundos")

    
