import objgraph
import pickle, gc, os, signal, threading, time, tracemalloc


gc.disable()


class A(object):
    pass


class B(object):
    pass


def test1():
    a = A()
    b = B()
    # print('inside_1', objgraph.count('A'))
    # print('inside_1', objgraph.count('B'))


def test2():
    a = A()
    b = B()
    a.child = b
    b.parent = a
    # print('inside_2', objgraph.count('A'))
    # print('inside_2', objgraph.count('B'))


test1()
# 对象应用已经回收
print('outside1_2', objgraph.count('A'))
print('outside1_2', objgraph.count('B'))


test2()
# 存在循环引用未被回收
# gc.collect()
print('Object count of A:', objgraph.count('A'))
print('Object count of B:', objgraph.count('B'))
print(gc.isenabled())


objgraph.show_backrefs(objgraph.by_type('A'), max_depth=10, filename='obj_A.png')
# ... run your application ...
tracemalloc.start()
test2()
# print('可回收对象', gc.DEBUG_COLLECTABLE)
# print('不可回收对象', gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
print(gc.garbage)
# 返回函数的16进制地址
print(hex(id(test2)))
# 返回所有被gc管理的对象
print(len(gc.get_objects()))
# 返回test2直接指向的对象
print(gc.get_referents(test2))
# 返回指向test2的对象
print(gc.get_referrers(test2))

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')


print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
# gc.disable() # 这里是否disable事实上无所谓
# gc.set_debug(gc.DEBUG_COLLECTABLE)
# for _ in range(1):
#     test2()
# print(gc.garbage)
# gc.collect()
print("**********")
# time.sleep(5)




class TakeSnapshot(threading.Thread):
    daemon = True

    def run(self):
        if hasattr(signal, 'pthread_sigmask'):
            # Available on UNIX with Python 3.3+
            signal.pthread_sigmask(signal.SIG_BLOCK, range(1, signal.NSIG))
        counter = 1
        while True:
            time.sleep(48)
            filename = ("./tracemalloc-%d-%04d.pickle"
                        % (os.getpid(), counter))
            print("Write snapshot into %s..." % filename)
            gc.collect()
            snapshot = tracemalloc.take_snapshot()
            with open(filename, "wb") as fp:
                # Pickle version 2 can be read by Python 2 and Python 3
                pickle.dump(snapshot, fp, 2)
            snapshot = None
            print("Snapshot written into %s" % filename)
            counter += 1


def func():
    li = []
    for i in range(50):
        li.append(i)
        time.sleep(1)


# save 25 frames

# tracemalloc.start(3)
# TakeSnapshot().start()
# func()
# with open(r'D:\work\AI-NLP\personal\内存管理工具\tracemalloc-7908-0001.pickle', mode='rb') as fp:
#     data = pickle.load(fp)
#     top_stats = data.statistics('lineno')
#     for stats in top_stats[:10]:
#         print(stats)
# print(data)