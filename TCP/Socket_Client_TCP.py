import socket
import random


host = '127.0.0.1'
port = 5000

interface_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

interface_s.connect((host,port))


#---------------------------------#
while True:
    pot = random.randint(0,29)
    choice = str(random.randint(10**pot, (10**(pot+1))-1))

    teste = input("Digite o comando SAIR caso queira sair, caso contrário,\na próxima string será enviada: ")
    if(teste.upper() == "SAIR"):
        print("fechando conexão com o servidor")
        interface_s.sendall(str.encode(teste))

    if(teste.upper() != "SAIR"):
        interface_s.sendall(str.encode(choice))
        data = interface_s.recv(1024)
        print('mensagem do servidor:',data.decode())

    else:
        break
