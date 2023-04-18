import socket
from time import sleep

host = 'localhost'
port = 5000

interface_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

interface_s.bind((host, port))

interface_s.listen()

print('aguardando conexão de cliente: ')

conn,ender = interface_s.accept()
print('Sucesso ao conectar com',ender)


#-----------------------------------------

while True:
    data = conn.recv(1024)

    if (data.upper() == str.encode('SAIR')):
        print('Fechando conexão')
        conn.close()
        break
    
    print(type(data))
    print(len(data))
    conn.sendall(data)

    sleep(0.75)