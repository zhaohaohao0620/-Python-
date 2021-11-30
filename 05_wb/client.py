from suds.client import Client


def clientTest():
    url = 'http://127.0.0.1:8080/?wsdl'

    req = {'demo1': 'client test'}

    client = Client(url)
    rsp = client.service.Test1(req)
    print(rsp)
    print(str(client.last_sent()))
    print(str(client.last_received()))


if __name__ == '__main__':
    clientTest()
