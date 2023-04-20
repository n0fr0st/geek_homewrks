import inspect
def myfunc(a, b, /, c, d, *args, e, f, **kwargs):
    pass

def inspect_func(func):
    print(f"функция - {func.__name__}")
    for param in inspect.signature(func).parameters.values():
        print(param.name, param.kind, sep=' - ')
inspect_func(myfunc)
