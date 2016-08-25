#! /usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from Constants.Constants import *

class MyApiClient:
    #TODO
    # creamos el socket
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ahora acemos que se conecte con el servidor
	clientsocket.connect((LOCALHOST,CHAT_PORT))
 
# este bucle hace que mientras este conectado  haga lo que pone en el interior
while 1:
        data = raw_input('>') #f uncion que hace que podamos escribir para mandarlo posteriormente
        clientsocket.send(data) # enviamos los dtaos que hemos escrito
        if not data: break # si no ai datos no lo envia
        newdata = clientsocket.recv(5000) # recibimos los datos que envie el servidor
        print 'servidor: %s' % newdata # y con esto lo escribimos en pantalla
clientsocket.close() # si no esta conectado cerramos el socket
 

"""********************
Función para enviar el mensaje
*********************"""
def client_message(self, mensaje)
	self.server.sendMessage_wrapper(texto)