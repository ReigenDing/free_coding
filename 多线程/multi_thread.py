'''
import os
import time
from threading import Thread


def run():
    print('run...%d...%d' % (os.getpid(), os.getppid()))
    time.sleep(4)
    print('run end')


def run2():
    print('run2...%d...%d' % (os.getpid(), os.getppid()))
    time.sleep(2)
    print('run2 end')


if __name__ == '__main__':
    t = Thread(target=run)
    t2 = Thread(target=run2)
    thread_list = []
    thread_list.append(t)
    thread_list.append(t2)
    for t in thread_list:
        t.setDaemon(True)
        t.start()
        t.join()
    print('main end')

'''
import os
import random
import time
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(threading.current_thread())
            print('thread {}, @number: {}---{}'.format(self.name, i, os.getpid()))
            time.sleep(random.choice([2]))


def main():
    print('pid---%s, ppid---%s, current---%s' % (os.getpid(), os.getppid(), threading.currentThread()))
    s = time.time()
    print("Start main threading")
    # 创建三个线程
    # threads = [MyThread() for i in range(4)]
    # # 启动三个线程
    # for t in threads:
    #     t.start()
    # t.join()
    time.sleep(random.choice([1, 2, 3, 4, 5]))
    print("End Main threading")
    end = time.time()
    return end-s


# def fib(n):
#     # print(n)
#     if n <= 1:
#         return 1
#     return fib(n-1)+fib(n-2)
#
# k = fib(4)
# print(k)

class A:
    def test(self) -> str:
        with ThreadPoolExecutor(max_workers=4) as executor:
            t = executor.map(main)
        for i in t:
            print(i)
        return 'ok'


class B:
    def test(self) -> str:
        with ProcessPoolExecutor(max_workers=4) as executor:
            t = executor.map(main, (1, 2, 3, 4), [5, 6, 7, 8], [1, 2, 3, 6])
        for i in t:
            print(i)
        return 'ok'


def run():
    a = B()
    a.test()


if __name__ == '__main__':
    a = A()
    a.test()







