import os

a = ('a', ',b', 'x')
print(str(a)[1: -1])
b = ','.join(a)
print(a, b)

import requests
from time import time


files = {
    "file": open("./test_date.pptx", "rb")
}
data = {"type": "案例", "tag": "案例", "uploader": "lwq",
        "public": "N",  'text': "哈哈哈啊哈哈哈啊哈哈哈哈啊哈哈哈"}
# # 887
# r = requests.post('http://10.66.57.60:5000/api/1.0/text/4in1', data=data, files=files)
# print(r.json())


def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    result = []
    for i in range(len(seats)):
        if seats[i] == 1:
            result.append(0)
        if seats[i] == 0:
            left_seats = seats[:i]
            right_seats = seats[i + 1:]
            try:
                left_dis = left_seats[::-1].index(1)
            except Exception as e:
                left_dis = len(left_seats)
            try:
                right_dis = right_seats.index(1)
            except Exception as e:
                right_dis = len(right_seats)
            min_dis = min(left_dis, right_dis)
            result.append(min_dis)
    seat_pos = max(result)
    return result.index(seat_pos)


# coding:utf-8
# author:Elvis

class TreeNode(object):
    def __init__(self):
        self.data = '#'
        self.l_child = None
        self.r_child = None


class Tree(TreeNode):
    # create a tree
    def create_tree(self, tree):
        data = input('->')
        if data == '#':
            tree = None
        else:
            tree.data = data
            tree.l_child = TreeNode()
            self.create_tree(tree.l_child)
            tree.r_child = TreeNode()
            self.create_tree(tree.r_child)

    # visit a tree node
    def visit(self, tree):
        # 输入#号代表空树
        if tree.data is not '#':
            print(str(tree.data) + '\t',)

    # 先序遍历
    def pre_order(self, tree):
        if tree is not None:
            self.visit(tree)
            self.pre_order(tree.l_child)
            self.pre_order(tree.r_child)

    # 中序遍历
    def in_order(self, tree):
        if tree is not None:
            self.in_order(tree.l_child)
            self.visit(tree)
            self.in_order(tree.r_child)

    # 后序遍历
    def post_order(self, tree):
        if tree is not None:
            self.post_order(tree.l_child)
            self.post_order(tree.r_child)
            self.visit(tree)


t = TreeNode()
tree = Tree()
tree.create_tree(t)
tree.pre_order(t)
print('\n')
tree.in_order(t)
print('\n')
tree.post_order(t)


# if __name__ == '__main__':
#     # s = time()
#     # k = maxDistToClosest([1,0,0,0])
#     # print(k)
#     # e = time()
#     # print(e-s)
#     fp = open('D:\work\AI-NLP\ExTriplesDocx\src\投标.docx', 'rb')
#     print(fp)
#     print(os.cpu_count())
#     import base64
#
#     data = 'hello, 世界vvvvvvvvvvvvvvvvvvvvvvvvvvvvv但是阿斯顿发深刻理解的覅偶安排vvvvvgsdgrdytrhdfgrtyhtujyedfgxdyhdtuhfdh'.encode()
#     based_data1 = base64.b64encode(data)
#     plain_data1 = base64.b64decode(based_data1)
#     based_data2 = base64.urlsafe_b64encode(data)
#     plain_data2 = base64.urlsafe_b64decode(based_data2)
#     print(based_data1)
#     print(based_data2)
#     print(plain_data1)
#     print(plain_data2)