import socket

host='127.0.0.1'
port=1500

clienteSocket=socket.socket()
clienteSocket.connect((host,port))

list_Candidatos = clienteSocket.recv(1024).decode()
print(list_Candidatos)

voto=input("->")
clienteSocket.send(voto.encode())

print('Contagem de votos')
data=clienteSocket.recv(1024)
contString= str(data, 'utf-8')
contString =contString.split("],")

print ("Votos por candidato")
for cont in contString:
    print(cont)
clienteSocket.close()
print('Conexão encerrada')