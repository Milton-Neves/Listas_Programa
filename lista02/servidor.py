import socket,threading

host='127.0.0.1'
port=1500

candidatos=[]

print('Cadastro: \n')
num_Candidatos= int(input('Candidatos '))
for i in range(num_Candidatos):
    candidato=input("Informe o número do candidato: ")
    candidatos.append([candidato,0])


servidor=socket.socket()
servidor.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1) 
servidor.bind((host,port))
print("...")


class ClientThread(threading.Thread): 
    def __init__(self,end_Cliente,socketCliente):
        threading.Thread.__init__(self)
        self.csocket=socketCliente
        self.end_Cliente=end_Cliente
        print("Conexão recebida de ",end_Cliente)


    def run(self):
        list_Candidatos= str(candidatos).encode()

        self.csocket.send(list_Candidatos)

        print('aguardando conexao')
        data=self.csocket.recv(1024).decode()
        voto_Recebido=int(data)


        for candidato in candidatos:
            if int(candidato[0]) == voto_Recebido:
                candidato[1] = candidato[1] + 1
                print("Recebeu de ",self.end_Cliente," o voto: ", voto_Recebido)

                list_Candidatos= str(candidatos).encode()
                self.csocket.send(list_Candidatos)
                break
        print('PARCIAL : ',candidatos)


while True:
    servidor.listen(1)
    clienteSocket,end_Cliente=servidor.accept()
    threadCliente=ClientThread(end_Cliente,clienteSocket)
    threadCliente.start()
servidor.close()