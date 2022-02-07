from spyne import (Application, Array, ServiceBase, Unicode,
                   UnsignedInteger, rpc)
from spyne.model.complex import ComplexModel
from spyne.model.primitive.number import Double
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class OutParam(ComplexModel):
    demo1 = UnsignedInteger
    demo2 = Double
    demo3 = Array(Double)
    demo4 = Unicode


class InParam(ComplexModel):
    demo1 = Unicode


class Demo(ServiceBase):
    """ 
   <ns0:Body>
      <ns1:Test1>                         ## _in_message_name
         <ns1:WSRequest>                  ## _in_variable_names
            <ns1:demo1></ns1:demo1>
         </ns1:WSRequest>
      </ns1:Test1>
   </ns0:Body>

   <tns:Test1Response>                  ## _out_message_name
      <tns:Test1Result>                 ## _out_variable_name
         <tns:demo1>255</tns:demo1>
         <tns:demo2>100.0</tns:demo2>
         <tns:demo3></tns:demo3>
         <tns:demo4>test</tns:demo4>
      </tns:Test1Result>
   </tns:Test1Response>

    """

    @rpc(InParam, _returns=OutParam)
    def Test1(self, WSRequest):
        print(WSRequest.demo1)

        rsp = OutParam()

        rsp.demo1 = 0xFF
        rsp.demo2 = 100.00
        rsp.demo3 = [1.0, 2.0, 3.0]
        rsp.demo4 = 'test'

        return rsp


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 8080
    application = Application([Demo],
                              tns='Demo',
                              in_protocol=Soap11(validator='lxml'),
                              out_protocol=Soap11())
    wsgi_app = WsgiApplication(application)
    server = make_server(ip, port, wsgi_app)
    server.serve_forever()
