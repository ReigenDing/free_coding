import sys
import tracemalloc
tracemalloc.start()
list1 = [1, 3, 4, 8, '数据', {'数据', 8}]
# print(id(list1))
# print(id(list1[0]))
# print(id(list1[3]))
# print(id(list1[5]))
# print(id(list1[4]))
print(sys.getsizeof(list1[5]))

memory = tracemalloc.get_traced_memory()
print(memory)

