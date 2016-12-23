# coding: utf-8
import numpy as np
import sys

sys.path.append('deep-learning-from-scratch')
from dataset.mnist import load_mnist

sys.path.append('deep-learning-from-scratch/ch05')
from two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True,
                                                  one_hot_label=True)

(train_size, input_size) = x_train.shape
output_size = t_train.shape[1]
iters_num = 10000
batch_size = 100
learning_rate = 0.1
iter_per_epoch = max(train_size / batch_size, 1)

network = TwoLayerNet(input_size=input_size,
                      hidden_size=50,
                      output_size=output_size)

train_loss_list = []
train_acc_list = []
test_acc_list = []

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    #grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)

    for key in network.params.keys():
        network.params[key] -= learning_rate * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc, test_acc)
