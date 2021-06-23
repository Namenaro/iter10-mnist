from utils import *

import numpy as np

class Descriptor:
    def __init__(self, side, checker):
        self.checker = checker
        self.side = side
        self.etalon_val = None
        self.max = None


    def apply(self, pic, x, y):
        sensory_array = get_sensory_array(pic, x, y, self.side)
        value = self.checker(sensory_array)
        abs_popravka = abs(self.etalon_val - value)
        normed_popravka =abs_popravka/self.max
        return normed_popravka

    def apply_to_pic(self, pic):
        ymax = pic.shape[0]
        xmax = pic.shape[1]

        res = np.zeros((ymax, xmax))
        for centery in range(0, ymax):
            for centerx in range(0, xmax):
                val = self.apply(pic, centerx, centery)
                res[centery, centerx] = val
        return res

def count_rescaling_coeff_for_popravka(descriptor, pics_for_stat):
    res = []
    for pic in pics_for_stat:
        res.append(descriptor.apply_to_pic(pic).flatten())
    res = np.array(res)
    return np.max(res)

def init_descriptor(etalon, x, y, side, checker, pics_for_stat):
    A = Descriptor(side, checker)
    sensory_array = get_sensory_array(etalon, x, y, side)
    A.etalon_val = A.checker(sensory_array)
    A.mean, A.std = count_rescaling_coeff_for_popravka(A, pics_for_stat)
    return A




