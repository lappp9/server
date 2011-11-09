from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sqlite3

# instantiate a server object
server_addr = ('localhost', 8000)
server = SimpleXMLRPCServer (server_addr, SimpleXMLRPCRequestHandler)
server.register_introspection_functions()

# define your methods in a class
class RPCMethods :

    message = "nothing here yet"
    
    def getMessage(self) :
	return message

    def setMessage(self, msg) :
        message = msg

# start the server
server.register_instance (RPCMethods ())

# here i should, make a player server object
# pass it to server.register_instance();
# then i can specify any player method right from the javascript
# no more python code needed

server.serve_forever ()
