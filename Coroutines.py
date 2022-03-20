from asyncio import sleep, get_event_loop, gather, create_task, run


class ChatUser:
    def __init__(self, msg_queue, name):
        self.__msg_queue = msg_queue
        self._name = name

    def get_msg(self):
        for msg in self.__msg_queue:
            print(f"{self._name} get {msg}")
            yield

    def send_msg(self):
        while True:
            print(self._name + " " + f"{self.__msg_queue}")
            self.__msg_queue.append(f"{self._name} {str(input())}")
            yield

    def generators(self):
        return self.send_msg(), self.get_msg()


class EventLoop:
    def __init__(self, *generators):
        self.__generators = generators

    def run_forever(self):
        while True:
            for generator in self.__generators:
                generator.send(None)



# message_queue = []  # Пустой список, который мы будем использовать в качестве очереди сообщений
# alex_user = ChatUser(message_queue, "alex")
# colin_user = ChatUser(message_queue, "colin")
# loop = EventLoop(*alex_user.generators(), *colin_user.generators())  # создаем нашу петлю событий
# loop.run_forever()  # просим нашу петлю бесконечно проходить по генераторам

async def send_message(name, msg):
    print(f"BEFORE {msg}")
    await sleep(1)
    print(f"{name} {msg}")


async def main_coro():
    await send_message("alex", "Здорова")
    await send_message("alex", "Здорова2")
    await send_message("alex", "Здорова3")


tasks = [send_message("alex", "Здорова"), send_message("alex", "Здорова2"), send_message("alex", "Здорова3")]


async def main_coro_two():
    await gather(*tasks)



async def taskcoro():
    for task in tasks:
        await task

# loop = get_event_loop()
# loop.run_until_complete(main_coro_two())
# run(taskcoro())

