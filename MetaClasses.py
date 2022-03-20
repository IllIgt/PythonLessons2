class A:
    a = 10

    def __init__(self):
        self.c = 30

    # def get_a(self):
    #     return self.a


print(type(A))

a = A()

print(type(a))

print(getattr(a, "a"))
print(getattr(a, "c"))
print(hasattr(a, "a"))
print(hasattr(a, "get_a"))
print(setattr(a, "b", 20))

print(a.b)

my_shiny_cls = type("MyShinyCls", (object,), {"a": 10, "b": 30})

msc = my_shiny_cls()
print(msc.a)
print(msc.b)
print(type(msc))



class MyMeta(type):
    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)


class A(metaclass=MyMeta):
    __metaclasss__ = MyMeta
    a = 10

    def __init__(self):
        self.c = 30

    def get_a(self):
        return self.a

print(A.__dict__)

a = A()

# print(a.a)
