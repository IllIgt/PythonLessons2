class OriginalHandler:
    def make_request(self):
        print("Hello everybody")


class Proxy:
    def __init__(self, oh: OriginalHandler):
        self._original_handler = oh

    def make_request(self):
        print("oh i am proxy")
        self._original_handler.make_request()
        print("Bye-bye")


class Server:
    def run(self, handler):
        handler.make_request()


oh = OriginalHandler()
prxy = Proxy(oh)


server = Server()

server.run(oh)
server.run(prxy)
