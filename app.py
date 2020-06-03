
from flask import Flask
from class_nodo import p2p_nodo
import sys
import time
"""----------------------------------------"""
app = Flask(__name__)


"""archivos donde se encuentran los modulos"""
sys.path.insert(0, '..') 

"""nodo """
node = p2p_nodo("142.44.246.92", 5001)

time.sleep(1)
node.start()
time.sleep(2)

"""-----  conocidos del nodo -----"""
node.connect_with_node('142.44.246.23', 5002)
node.connect_with_node('142.44.246.12', 5003)
node.connect_with_node('158.69.63.154', 5004)

time.sleep(2)

node.send_to_nodes({"message": "Hola soy gibraltar!"})
    

