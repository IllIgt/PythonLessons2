from functools import wraps


class MyClass(object):
    pass


def my_func():
    my_func.a += 2
    print(f"i'm func {my_func.a}")


my_func.a = 10


func_obj = my_func

# func_obj()


def my_second_func(some_func):
    print("i'am in second func, calling some func")
    some_func()


# my_second_func(my_func)


class Decorator:
    def __init__(self, obj):
        self.wrapped_obj = obj

    def do_something(self):
        self.wrapped_obj.do_something()


class SendDataDecorator(Decorator):

    def do_something(self):
        data = self.wrapped_obj.do_something()
        print(f"i' am get data from obj and send it {data}")
        return data


class EncodeDataDecorator(Decorator):

    def do_something(self):
        data = self.wrapped_obj.do_something()
        data = "Encoded_" + data
        print(f"i'a, get data and encode this {data}")
        return data


class TimeStampDecorator(Decorator):

    def do_something(self):
        current_time = "start_time "
        data = self.wrapped_obj.do_something()
        end_time = " end_time"
        print(f"i'am timestamped data: {current_time}, {data}, {end_time}")
        return current_time + data + end_time


class DataProvider:

    def do_something(self):
        return "i am give ypu some data"


# provider = DataProvider()
# time_stamp = TimeStampDecorator(provider)
# encode_decorator = EncodeDataDecorator(time_stamp)
# send_decorator = SendDataDecorator(encode_decorator)
# send_decorator.do_something()


def send_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        print(func.__name__ + " was called")
        print(f"i' am get data from obj and send it {data}")
        return data
    return wrapper


def exception_dec(func):
    @wraps(func)
    def wrapper():
        raise Exception("DECOR EXCEPTION")
    return wrapper


# @exception_dec
# @send_data
# def data_provider(a):
#     return f"i give you some data {a}"

# send_data(data_provider)


def decorator_factory(argument):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"do sometnig with {argument}")
            data = func(*args, **kwargs)
            print(f"do something with data {data}")
            # return data
        return wrapper
    return decorator


@decorator_factory("test dataq")
def data_provider(a):
    return f"i give you some data {a}"


# print(data_provider.__name__)
print(data_provider(12))
# print(send_data(data_provider)(12))
print("END")