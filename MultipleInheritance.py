class MyMixin:
    def __init__(self):
        self.additional_field = "my_mixin"


class A:
    a = 10

    def get_a(self):
        return self.a


print(A.__mro__)


class B(A):
    b = 20

    def get_a(self):
        return "I am your toy, master"

    def get_b(self):
        return self.b


print(B.__mro__)


class C(A):
    c = 30

    def get_a(self):
        return "I am not your toy, stupid sexist"

    def get_c(self):
        return self.c


print(C.__mro__)


class D(B, C):
    d = 40

    def get_d(self):
        return self.d


print(D.__mro__)

d = D()
print(d.get_a())


class G(D, MyMixin):
    pass


g = G()

print(g.additional_field)


class MetaFirst(type):
    pass


class MetaSecond(type):
    pass


class N(metaclass=MetaFirst):
    pass


class M(metaclass=MetaSecond):
    pass


class MetaMN(MetaFirst, MetaSecond):
    pass


class MN(M, N, metaclass=MetaMN):
    pass


mn = MN()
