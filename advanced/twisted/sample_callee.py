from twisted.internet import protocol, reactor


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    def dataReceived(self, data):
        "As soon as any data is received, write it back. Callee."
        self.transport.write(data)


class EchoFactory(protocol.ServerFactory):
    protocol = Echo


def main():
    """This runs the protocol on port 8000"""
    factory = EchoFactory()
    # reactorはSingleton
    reactor.listenTCP(8000, factory)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == "__main__":
    main()
