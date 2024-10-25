def decorator(func):
    return func

@decorator
def decorator_example():
    print('Привет, Вселенная')

decorator_example()

decorator_example = decorator(decorator_example)
