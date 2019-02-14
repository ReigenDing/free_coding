import sys

import tensorflow as tf

# 训练数据、
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [[0], [0], [0], [1]]

#定义网络结构
N_INPUT_MODES = 2
N_OUTPUT_MODES = 1

# 定义训练迭代次数
N_STEPS = 2000
N_EPOCH = 100

# 定义学习率，即每次递减下降的大小
LEARNING_RATE = 0.02

# 定义接受数据的占位符
x_ = tf.placeholder(tf.float32, shape=[len(X), N_INPUT_MODES], name='x_input')
y_ = tf.placeholder(tf.float32, shape=[len(Y), N_OUTPUT_MODES], name='y_output')

# 定义权重和偏置
weight = tf.Variable(tf.random_uniform([N_INPUT_MODES, N_OUTPUT_MODES], -1, 1), name='weight')
bias = tf.Variable(tf.zeros([N_OUTPUT_MODES]), name='bias')
print(weight, bias)
print(tf.random_uniform([N_INPUT_MODES, N_OUTPUT_MODES], -1, 1))
# 定义前向函数
output = tf.sigmoid(tf.matmul(x_, weight) + bias)

# 定义损失函数（最小均方差）， 来描述预测值和真实之间的差距
cost = tf.reduce_mean(tf.square(Y - output))
print(cost)

# 定义反向传播函数，即使用梯度下降的方法，求解损失函数的最小值
train = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cost)

# 初始化变量
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 开始训练过程
for i in range(N_STEPS):
    # 执行训练函数， 讲训练数据feed到模型中
    sess.run(train, feed_dict={x_: X, y_: Y})
    if i % N_EPOCH == 0:
        # 每隔N_EPOCH轮输出一次训练结果
        print('weight:', sess.run(weight), 'bias: ', sess.run(bias))
        print('STEPS: ', i, 'cost: ', sess.run(cost, feed_dict={x_: X, y_: Y}))
        # sys.stdout.write('STEPS: {}, cost: {}'.format(i, sess.run(cost, feed_dict={x_: X, y_: Y})))

# 训练结束，执行一次预测，并查看结果
print('output: ', sess.run(output, feed_dict={x_: X, y_: Y}))
print(tf.get_default_graph())
print(x_.graph)

# sess = tf.Session()
result = x_ + y_
with sess.as_default():
    print(result.eval())