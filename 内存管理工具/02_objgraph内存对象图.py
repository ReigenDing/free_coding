# -*- coding: utf-8 -*-
import objgraph

_cache = []


class OBJ(object):
    pass


def func_to_leak():
    o = OBJ()
    _cache.append(o)
    # do something with o, then remove it from _cache

    if True: # this seem ugly, but it always exists
        return
    _cache.remove(o)


if __name__ == '__main__':
    print(type(func_to_leak))
    print('counter OBJ:', objgraph.count('OBJ'))
    print('counter func_to_leak:', objgraph.count('function'))
    objgraph.show_growth()
    try:
        func_to_leak()
    except:
        pass
    print('after call func_to_leak')
    # 统计该类型对象的数目
    print('counter OBJ:', objgraph.count('OBJ'))
    print('counter func_to_leak:', objgraph.count('function'))
    # 更具对象类型返回对象列表
    print('999999999', objgraph.by_type('str'))
    # 打印实例化做多的前10个对象
    print(objgraph.show_most_common_types(10))
    # 统计自上次调用以来增加得最多的对象，这个函数非常有利于发现潜在的内存泄露
    objgraph.show_growth()
    # 生产一张有关objs的引用图，看出看出对象为什么不释放，后面会利用这个API来查内存泄露
    objgraph.show_backrefs(objgraph.by_type('OBJ')[0], max_depth=10, filename='obj.png')
    # 找到一条指向obj对象的最短路径，且路径的头部节点需要满足predicate函数 （返回值为True）
    objgraph.show_chain(objgraph.find_backref_chain(objgraph.by_type('OBJ')[0], objgraph.is_proper_module), filename='short_chain.png')
