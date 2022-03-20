from abc import ABC, abstractmethod


class MyBaseCls(ABC):
    name = "default"

    @abstractmethod
    def print_some_text(self):
        print("opa")


class IBase(ABC):

    @abstractmethod
    def print(self):
        pass


# abstract = MyBaseCls()


class MyABC:

    def some_func(self):
        raise NotImplementedError


abstract = MyABC()
abstract.some_func()


class MyConcreteClass(MyBaseCls):

    def print_some_text(self):
        # pass
        super().print_some_text()
        print("Some text")


my_concrete_class = MyConcreteClass()

my_concrete_class.print_some_text()
print(my_concrete_class.name)
