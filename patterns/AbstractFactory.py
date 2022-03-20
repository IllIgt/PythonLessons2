from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class FancyFactory(AbstractFactory):

    def create_chair(self):
        print("Fancy chair")

    def create_table(self):
        print("Fancy table")


class BrokeAssFactory(AbstractFactory):

    def create_chair(self):
        print("BrokeAss chair")

    def create_table(self):
        print("BrokeAss table")


def make_some_furniture(factory: AbstractFactory):
    factory.create_table()
    factory.create_chair()


fancy = FancyFactory()

make_some_furniture(fancy)


poor_guy = BrokeAssFactory()

make_some_furniture(poor_guy)




