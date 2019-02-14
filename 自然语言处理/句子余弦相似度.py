

def levenshtein(first, second):
    ''' 编辑距离算法（LevD）
        Args: 两个字符串
        returns: 两个字符串的编辑距离 int
    '''
    if len(first) > len(second):
        first, second = second, first
    if len(first) == 0:
        return len(second)
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [list(range(second_length)) for x in range(first_length)]
    print(distance_matrix)
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i - 1][j] + 1
            insertion = distance_matrix[i][j - 1] + 1
            substitution = distance_matrix[i - 1][j - 1]
            if first[i - 1] != second[j - 1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
            print(distance_matrix)
    return distance_matrix[first_length - 1][second_length - 1]


import math
import re
import datetime
import time

text1 = "This game is one of the very best. games ive  played. the  ;pictures? " \
        "cant descripe the real graphics in the game."
text2 = "this game have/ is3 one of the very best. games ive  played. the  ;pictures? " \
        "cant descriPe now the real graphics in the game."
text3 = "So in the picture i saw a nice size detailed metal puzzle. Eager to try since I enjoy 3d wood puzzles, i ordered it. Well to my disappointment I got in the mail a small square about 4 inches around. And to add more disappointment when I built it it was smaller than the palm of my hand. For the price it should of been much much larger. Don't be fooled. It's only worth $5.00.Update 4/15/2013I have bought and completed 13 of these MODELS from A.C. Moore for $5.99 a piece, so i stand by my comment that thiss one is overpriced. It was still fun to build just like all the others from the maker of this brand.Just be warned, They are small."
text4 = "I love it when an author can bring you into their made up world and make you feel like a friend, confidant, or family. Having a special child of my own I could relate to the teacher and her madcap class. I've also spent time in similar classrooms and enjoyed the uniqueness of each and every child. Her story drew me into their world and had me laughing so hard my family thought I had lost my mind, so I shared the passage so they could laugh with me. Read this book if you enjoy a book with strong women, you won't regret it."


def compute_cosine(text_a, text_b):
    # 找单词及词频
    words1 = text_a.split(' ')
    words2 = text_b.split(' ')
    # print(words1)
    words1_dict = {}
    words2_dict = {}
    for word in words1:
        # word = word.strip(",.?!;")
        word = re.sub('[^a-zA-Z]', '', word)
        word = word.lower()
        # print(word)
        if word != '' and word in words1_dict:  # 这里改动了
            num = words1_dict[word]
            words1_dict[word] = num + 1
        elif word != '':
            words1_dict[word] = 1
        else:
            continue
    for word in words2:
        # word = word.strip(",.?!;")
        word = re.sub('[^a-zA-Z]', '', word)
        word = word.lower()
        if word != '' and word in words2_dict:
            num = words2_dict[word]
            words2_dict[word] = num + 1
        elif word != '':
            words2_dict[word] = 1
        else:
            continue
    print(words1_dict)
    print(words2_dict)

    # 排序
    dic1 = sorted(words1_dict.items(), key=lambda asd: asd[1], reverse=True)
    dic2 = sorted(words2_dict.items(), key=lambda asd: asd[1], reverse=True)
    print(dic1)
    print(dic2)

    # 得到词向量
    words_key = []
    for i in range(len(dic1)):
        words_key.append(dic1[i][0])  # 向数组中添加元素
    for i in range(len(dic2)):
        if dic2[i][0] in words_key:
            # print 'has_key', dic2[i][0]
            pass
        else:  # 合并
            words_key.append(dic2[i][0])
    # print(words_key)
    vect1 = []
    vect2 = []
    for word in words_key:
        if word in words1_dict:
            vect1.append(words1_dict[word])
        else:
            vect1.append(0)
        if word in words2_dict:
            vect2.append(words2_dict[word])
        else:
            vect2.append(0)
    print(vect1)
    print(vect2)

    # 计算余弦相似度
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(vect1)):
        sum += vect1[i] * vect2[i]
        sq1 += pow(vect1[i], 2)
        sq2 += pow(vect2[i], 2)
    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0
    # print(result)
    return result


if __name__ == '__main__':
    result = compute_cosine(text1, text2)
    print(result)




