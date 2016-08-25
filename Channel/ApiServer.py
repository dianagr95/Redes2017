#! /usr/bin/env python
# -*- coding: utf-8 -*

import SimpleXMLRPCServer
from Constants.Constants import *
i

class MyApiServer:
    def __init__(self, my_port = None):
       self.server = SimpleXMLRPCServer.SimpleXMLRPCServer((LOCALHOST, my_port), allow_none=True)


class FunctionWrapper:
    def __init__(self):
        print ""
        #TODO

     """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        self.interfaz.plainTextEdit.insertPlainText("Contacto: "+message+ "\n")
        print message
 
	def serve(self):
        self.server.serve_forever()


