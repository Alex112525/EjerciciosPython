from Ejercicio4 import Tcp
from  Ejercicio4 import Udp

#cliente = Tcp.TCPclient()  #Prueba envio de mensaje TCP
#cliente.sedmsg("Aloo")
#print(cliente.getmsg())

#cliente2 = Tcp.TCPclient() #Prueba de apagado de servidor TCP
#cliente2.sedmsg("offServer")
#print(cliente2.getmsg())

#cliente = Udp.UDPclient()  #Prueba envio de mensaje UDP
#cliente.sendmsg(msg="offServer")

cliente = Udp.UDPclient()   #Prueba de apagado de servidor UDP
cliente.sendmsg(msg="offServer")
