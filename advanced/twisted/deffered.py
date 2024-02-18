from twisted.internet.defer import Deferred


def got_poem(res):
    print('Your poem is served:')
    print(res)


def poem_failed(err):
    print('No poetry for you.')


def poem_done(_):
    from twisted.internet import reactor
    reactor.stop()


deffer = Deferred()  # type: ignore

# add a callback/err-back pair to the chain
deffer.addCallbacks(got_poem, poem_failed)
deffer.addBoth(poem_done)

# fire the chain with a normal result
# deffer.callback('This poem is short.')
# deffer.errback(Exception('Error'))

from twisted.internet import reactor

reactor.callWhenRunning(deffer.callback, 'Another short poem.')
reactor.run()

print("Finished")
