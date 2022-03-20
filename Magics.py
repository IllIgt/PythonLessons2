from pprint import pprint


class MySingleton:
    def __init__(self, a=0):
        self.a = a

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MySingleton, cls).__new__(cls)
        return cls.instance


sngl = MySingleton(12)
sngl.instance
print(sngl.a)
print(id(sngl))
print("--------------------------")
sngl2 = MySingleton()
print(sngl.a)
print(id(sngl))
print(sngl2.a)
print(id(sngl2))
print("--------------------------")
sngl3 = MySingleton(100)

print(sngl.a)
print(sngl2.a)
print(sngl3.a)


print(id(sngl))
print(id(sngl2))
print(id(sngl3))
