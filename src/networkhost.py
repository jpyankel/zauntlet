import socket
class NetworkHost ():
    """
        A host is both a client and server running on the same machine.
        This class controls both the localplayer and server functionality.
        The host player will manage an instance of a NetworkHost.
    """
    def __init__ (self, port=8888):
        server = socket.socket() # Create socket server
        hostIP = socket.gethostname()
        server.bind(hostIP) # Start listening on our localhost
