from socket import socket, gethostname, gethostbyname, AF_INET, SOCK_DGRAM


class Sock:
    def __init__(self):
        self.ip = gethostbyname(gethostname())
        self.port = 2088

    def udp_server_recv(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind((self.ip, self.port))
        sock.bind(5)

        while True:
            msg = sock.recvfrom(1024)
            print(msg)

    def tcp_client(self, msgs):
        client = socket(AF_INET, SOCK_DGRAM)
        client.sendto(msgs, (self.ip, self.port))
