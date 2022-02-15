from socket import socket, gethostname, gethostbyname, AF_INET, SOCK_STREAM


class Sock:
    def __init__(self):
        self.ip = gethostbyname(gethostname())
        self.port = 2088

    def tcp_server_recv(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.bind(5)

        while True:
            self.connect, addr = sock.accept()
            print(addr)
            while True:
                try:
                    msg = self.connect.recv(1024)

                    print(len(msg))
                except:
                    break

    def tcp_server_send(self, msgs):
        try:
            if not self.connect.close:
                self.connect.send(msgs)
            else:
                print("已断开")
        except:
            pass

    def tcp_client(self, msgs):
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((self.ip, self.port))
        while True:
            print(client.recv(1024))

            client.send(msgs)
            break
        client.close()
