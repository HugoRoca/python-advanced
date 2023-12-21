# def tree_decorator(func):
#     def lights():
#         print("Lights")
#
#     def star():
#         print("Star")
#
#     lights()
#     star()
#     return func
#
#
# @tree_decorator
# def tree():
#     print("I'm a tree")
#
# tree()

class A:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, args):
        print("Edit attr")
        self.__name = args

    @name.getter
    def name(self):
        print("Return attr")
        return self.__name

    @name.deleter
    def name(self):
        print("Delete attr")
        del self.__name


a = A("Hugo")
print(a.name)

a.name = "Candy"
print(a.name)

del a.name


class cls_decorator:
    @classmethod
    def setter(self, func):
        print("I'm decorating")
        return func

    @staticmethod
    def getter(func):
        print("I'm getter")
        return func


@cls_decorator.getter
def sing():
    print("I'm sing")

sing()
