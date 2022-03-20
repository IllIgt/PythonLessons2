from pprint import pprint


class CallMeta(type):
    def __call__(self, *args, **kwargs):
        print("meta call")
        return super(CallMeta, self).__call__(*args, **kwargs)


class MySingleton(metaclass=CallMeta):

    def __init__(self, a=0):
        print("init")

        self.a = a

    def __new__(cls, *args, **kwargs):
        print("new")

        if not hasattr(cls, 'instance'):
            cls.instance = super(MySingleton, cls).__new__(cls)
        return cls.instance

    def __call__(self, *args, **kwargs):
        print("call")


ms = MySingleton()
ms()


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

        return instances[class_]

    return getinstance


@singleton
class DecoratedSingleton:
    def __init__(self, a=0):
        self.a = a


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingletonSecond(metaclass=Singleton):
    def __init__(self, a=0):
        self.a = a


mss = MySingletonSecond.__call__()
print(mss)

sngl = DecoratedSingleton(12)
print(sngl.a)
print(id(sngl))
print("--------------------------")
sngl2 = DecoratedSingleton()
print(sngl.a)
print(id(sngl))
print(sngl2.a)
print(id(sngl2))
print("--------------------------")
sngl3 = DecoratedSingleton(100)

print(sngl.a)
print(sngl2.a)
print(sngl3.a)

print(id(sngl))
print(id(sngl2))
print(id(sngl3))

sngl = MySingletonSecond(12)
print(sngl.a)
print(id(sngl))
print("--------------------------")
sngl2 = MySingletonSecond()
print(sngl.a)
print(id(sngl))
print(sngl2.a)
print(id(sngl2))
print("--------------------------")
sngl3 = MySingletonSecond(100)
print(sngl.a)
print(sngl2.a)
print(sngl3.a)

print(id(sngl))
print(id(sngl2))
print(id(sngl3))
