class Publisher:
    def __init__(self):
        self._subscribers = []
        self._msg = ""

    def subscribe(self, sub):
        self._subscribers.append(sub)

    def get_msg(self, msg):
        self._msg = msg

    def notify_subscribers(self):
        for sub in self._subscribers:
            sub.notify(self._msg)


class Subscriber:
    def notify(self, msg):
        print(f"i'am notified with {msg}")


class Coordinator:
    def __init__(self, pub):
        self._p = pub

    def process_message(self, msg):
        self._p.get_msg(msg)
        self._p.notify_subscribers()


p = Publisher()

sub1 = Subscriber()
sub2 = Subscriber()
sub3 = Subscriber()

p.subscribe(sub1)
p.subscribe(sub2)
p.subscribe(sub3)


c = Coordinator(p)
c.process_message("Hola! new message")
