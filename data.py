import numpy as np

import torchvision.datasets as datasets

def get_train_mnist():
    mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
    return mnist_trainset


def _get_exact_numbers(the_number, np_images, np_labels):
    results = []
    for i in range(len(np_labels)):
        if np_labels[i] == the_number:
            results.append(np_images[i])
    return np.array(results)


def get_numbers_of_type(the_number):
    mnist_train = get_train_mnist()
    np_images = mnist_train.train_data.numpy()
    np_labels = mnist_train.train_labels.numpy()
    return _get_exact_numbers(the_number, np_images, np_labels)


def etalons_of3():
    np_images = get_numbers_of_type(the_number=3)
    indexes = [34,32,25,67,68,35,210,314,420, 496,620,659,635,667,733,715]
    exemplars = list([np_images[ind] for ind in indexes])
    #draw_several(exemplars, indexes, rows=2, cols=int(len(indexes)/2))
    return exemplars

def etalons_of1():
    np_images = get_numbers_of_type(the_number=1)
    indexes = [0,7,28,18,27,41,76,98]
    exemplars = list([np_images[ind] for ind in indexes])
    #draw_several(exemplars, indexes, rows=2, cols=int(len(indexes) / 2))
    return exemplars

def etalons_of1_little():
    np_images = get_numbers_of_type(the_number=1)
    indexes = [94,101,100]
    exemplars = list([np_images[ind] for ind in indexes])
    #draw_several(exemplars, indexes, rows=1, cols=int(len(indexes) ))
    return exemplars

def etalons_of4():
    np_images = get_numbers_of_type(the_number=4)
    indexes = [94,101,100]
    exemplars = list([np_images[ind] for ind in indexes])
    #draw_several(exemplars, indexes, rows=1, cols=int(len(indexes) ))
    return exemplars

def etalons_of6():
    np_images = get_numbers_of_type(the_number=6)
    indexes = [220,221,222,235,330]
    exemplars = list([np_images[ind] for ind in indexes])
    #draw_several(exemplars, indexes, rows=1, cols=int(len(indexes) ))
    return exemplars

def get_diverse_set_of_numbers(n):
    mnist_train = get_train_mnist()
    np_images = mnist_train.train_data.numpy()[0:n]
    #draw_several(np_images[0:35], list(range(0,35)), rows=5, cols=7)
    return np_images