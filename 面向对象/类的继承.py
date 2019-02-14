class A:
    def __init__(self, q, p):
        print('A init')
        self.k = q
        self.g = p

    def run(self):
        print('function run %d%d' % (self.k, self.g))


class B(A):
    def __init__(self):
        super(B, self).__init__(4, 5)
        print('B init')

    def test222(self):
        ug = 1/0
        print('test func')

    def __enter__(self):
        print('enter function')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit function')
        print('#'.center(30, '-'))
        print(exc_tb)
        print(exc_val)
        print(exc_type)
        print('#'.center(30, '-'))


# ins = B()
# ins.run()
with B() as k_func:
    k_func.test222()
