def decorator(func):
    def new_func():
        print('Казнить нельзя, помиловать')

    return new_func

@decorator
def decorate_example():
    print('Казнить, нельзя помиловать')

print(decorate_example.__class__)
print(decorate_example.__name__)