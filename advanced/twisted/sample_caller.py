from twisted.internet import protocol, reactor
from twisted.internet import defer


class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):
        self.transport.write(b"hello, world!")

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("Server said:", data)
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print("connection lost")


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def __init__(self, deferred):
        self.deferred = deferred

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        # reactor.stop()
        self.deferred.errback(reason)

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        # reactor.stop()
        self.deferred.callback("OK")


def get_echo(host, port):
    d = defer.Deferred()
    from twisted.internet import reactor
    factory = EchoFactory(d)
    reactor.connectTCP(host, port, factory)
    return d


# this connects the protocol to a server running on port 8000
def main():
    def callback(message):
        reactor.stop()
        print(f"Reactor stopped. {message}")

    def error(message):
        reactor.stop()
        print(f"Reactor error stopped. {message}")

    d = get_echo("localhost", 8000)
    d.addCallbacks(callback, error)

    reactor.run()


if __name__ == "__main__":
    main()
    print('End')
