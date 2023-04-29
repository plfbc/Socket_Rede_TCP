import socket
import Funcoes_Server_TCP as FST
host = 'localhost'
port = 5000

while True:
    
    interface_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    interface_s.bind((host, port))

    interface_s.listen()

    print('aguardando conexão de cliente: ')

    conn,ender = interface_s.accept()
    print('Sucesso ao conectar com',ender)


    #-----------------------------------------

    data = conn.recv(1024)

    str_cli = str(data.decode())
    str_resp = FST.server_resp(str_cli)

    str_resp = str.encode(str_resp)

    conn.sendall(str_resp)


    conn.close()