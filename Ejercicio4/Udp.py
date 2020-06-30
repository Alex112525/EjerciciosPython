import socket as s


class UDPserver:
    udp = ""

    def __init__(self):
        self.udp = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.udp.bind(("127.0.0.1", 12345))
        status = True
        while status:
            print("Waiting pakages")
            data, addr = self.getmsg()
            if data:
                print(f"message received {data}, from {addr}")
                if data == b"offServer":
                    self.sendmsg(addr, "Shutting down server")
                    print("Shutting down server")
                    status = False
                else:
                    self.sendmsg(addr, "message received")

    def sendmsg(self, addr="127.0.0.1", msg="default"):
        self.udp.sendto(msg.encode(), addr)

    def getmsg(self):
        return self.udp.recvfrom(1024)


class UDPclient:
    udpc = s.socket(s.AF_INET, s.SOCK_DGRAM)

    def sendmsg(self, addr=("127.0.0.1", 12345), msg="default"):
        self.udpc.sendto(msg.encode(), addr)
        print("Mensaje enviado")

    def getmsg(self):
        data, addr = self.udpc.recvfrom(1024)
        return data, addr


if __name__ == "__main__":
    Server = UDPserver()
