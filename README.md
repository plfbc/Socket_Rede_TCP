# Socket_Rede_TCP

> Trabalho de Redes de Computadores do 5º semestre de Engenharia de Software.


# **Criadores**:
### Paulo Victor Alves Fabricio
### Pedro de Carvalho Chaaban
<br></br>

# **Os SOCKETs**: 
> Nessa representação de sockets de redes da camada de aplicação teram 2 sockets:
>- Socket Cliente: Socket_Client_TCP: Responsavel por fazer as requisições e receber respostas do server, 
> no caso gerar um número de até 30 dígitos e envia-lo, essa ação repete a cada 10 segundos.

<br></br>
>- Socket Servidor: Socket_Server_TCP: Responsável por receber as requisições do cliente e enviar resposta,
> no caso verifica se o número gerado tem até 10 digitos, assim verificando se ele é par ou impar, caso tenha mais de 10 gera uma string aleatoria usando as bibliotecas 
string e random.

<br></br>
### as funções de cada socket podem sem encontradas em seus respequitivos arquivos de funções.
