def func1(args):
    print(args)


func1("test")


def func2(name: "definir como string"):
    print(name)


func2("hugo")


def func3(name: str) -> str:
    return name


print(func3("func3"))


# func sum
def sum(n1: int, n2: int) -> int:
    return n1 + n2


print(sum(1, 3))

# props
def argumments(*args):
    print(args)


argumments((1, 2, 3, 4), "qw")


def kwargumment(**kwargs):
    print(kwargs)


kwargumment(a=1, b=2, c="hi")