from collections.abc import Iterable


class PythonIterator:
    def __init__(self, collection):
        self.collection = collection

    def __next__(self):
        current_leaf = self.collection
        if current_leaf.next_leaf is None:
            raise StopIteration()
        self.collection = current_leaf.next_leaf
        return current_leaf.value


class Leaf(Iterable):
    def __init__(self, value, next_leaf):
        self.value = value
        self.next_leaf = next_leaf

    def __iter__(self):
        return PythonIterator(self)


leaf = Leaf(1, Leaf(2, Leaf(3, Leaf(4, None))))

# for i in leaf:
#     print(i)
# print(leaf.value)
# print(leaf.next_leaf.value)
# print(leaf.next_leaf.next_leaf.value)
# print(leaf)


class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.current_leaf = collection

    def next(self):
        if not self.is_stopped():
            self.current_leaf = self.current_leaf.next_leaf
        else:
            return False

    def get_current_leaf(self):
        return self.current_leaf

    def is_stopped(self):
        return self.current_leaf.next_leaf is None


iterator = Iterator(leaf)

start_leaf = iterator.get_current_leaf()
# print(iterator.get_current_leaf().value)
# iterator.next()
# print(iterator.get_current_leaf().value)


def my_simple_generator():
    n = 1
    c = 1
    while c <= 100:
        result = n + c
        yield result
        n, c = c, result


for i in my_simple_generator():
    print(i)


print([i for i in my_simple_generator()])