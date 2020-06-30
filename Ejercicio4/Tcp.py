import socket as s


class TCPserver:
    def __init__(self):
        tcp = s.socket()
        server_address = ("127.0.0.1", 35495)
        tcp.bind(server_address)

        tcp.listen()
        status = True
        while status:
            print("waiting for connection")
            self.connection, self.client_address = tcp.accept()
            print(f"client adress {self.client_address}")
            while True:
                data = self.getmsg()
                print(data)
                if data != b"":
                    if data == b"offServer":
                        self.sendmsg("Shutting down server")
                        print("Shutting down server")
                        status = False
                    else:
                        self.sendmsg("Message received")
                    self.connection.close()
                    break

    def sendmsg(self, msg):
        msg = msg.encode()
        self.connection.send(msg)

    def getmsg(self):
        if self.connection:
            return self.connection.recv(16)
        else:
            return -1


class TCPclient:
    tcpc = s.socket()

    def __init__(self):
        self.tcpc.connect(("127.0.0.1", 35495))
        print("Connected to the server")

    def sedmsg(self, msg):
        msg = msg.encode()
        self.tcpc.send(msg)
        print("Message sent")

    def getmsg(self):
        return self.tcpc.recv(1024)


if __name__ == "__main__":
    server = TCPserver()

