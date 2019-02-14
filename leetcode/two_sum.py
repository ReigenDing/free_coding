#! coding=utf-8


def two_sum(nums, target):
    for index_i, i in enumerate(nums):
        for index_j, j in enumerate(nums):
            if index_i != index_j and i+j == target:
                return index_i, index_j


def add_numbers(list1, list2):
    result = []
    temp = 0
    for i, j in zip(list1, list2):
        s = i + j + temp
        if s > 9:
            s = s % 10
            temp = 1
        else:
            temp = 0
        result.append(str(s))
    return ''.join(result)




if __name__ == '__main__':
    a = add_numbers([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7])
    print(a)









