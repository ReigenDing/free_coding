

def outer(func):
    def inner(name):
        print('name:', name)
        return func()
    return inner


@outer
def main():
    print('main')


main(name='ding')



