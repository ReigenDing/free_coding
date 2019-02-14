# -*- coding: utf-8 -*-
import objgraph, sys


class OBJ(object):
    pass


def direct_cycle_reference():
    a = OBJ()
    a.attr = a
    objgraph.show_backrefs(objgraph.by_type('OBJ')[0], max_depth=5, filename="frame_direct.png")


if __name__ == '__main__':
    direct_cycle_reference()
