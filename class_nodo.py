
from p2pnetwork.node import Node

class p2p_nodo(Node):# es node ya que es la importacion de la libreria 

    """ crear un archivo cliente """
    archivo = open("num.txt","w")
    archivo.close()
    

    def __init__(self, host, port):

        super(p2p_nodo, self).__init__(host, port, None)
        print("Nodo Conectado")# posivilidad de quitar


    def node_message(self, node, data):

        archivo = open("num.txt","a")
        archivo.write("{},0".format(str(data)))
        archivo.close() 

