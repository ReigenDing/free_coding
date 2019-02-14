# -*- coding: utf-8 -*-
import weakref
import objgraph


class OBJ(object):
    def f(self):
        print('HELLO')


if __name__ == '__main__':
    o = OBJ()
    w = o
    objgraph.show_backrefs(objgraph.by_type('OBJ'), max_depth=10, filename='./弱引用.png')
    w.f()
    del o
    w().f()