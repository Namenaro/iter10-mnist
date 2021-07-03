from A import *
from hypothesys import *

from scipy.stats import entropy
import numpy as np
import matplotlib.pyplot as plt

def get_probabilities_digitized(activations_list, max, nbins):
    activations = np.array(activations_list)
    (probs, bins, _) = plt.hist(activations, bins=nbins,
                                weights=np.ones_like(activations) / len(activations), range=(0, max))
    plt.show()
    return probs


def measure_discrim_power_of_hypo_onto_descr(pics, hypothesys, descriptor, nbins):
    Afields = []
    ABfields = []
    for pic in pics:
        Afield = descriptor.apply_to_pic(pic)
        Bfield = hypothesys.apply_to_all_pic(pic)
        ABfield = Afield * Bfield
        Afields = Afields + Afield.flatten().tolist()
        ABfields = ABfields + ABfield.flatten().tolist()
    Afields_hist = get_probabilities_digitized(Afields, 1, nbins)
    AB_fields_hist = get_probabilities_digitized(ABfields, 1, nbins)
    discrim_power = measure_discrim_power(Afields_hist, AB_fields_hist)
    return discrim_power



def measure_discrim_power(Afields_hist, AB_fields_hist):
    w=1
    sum=0 #чем больше тем лучше
    for i in range(len(Afields_hist)-1,-1,-1):
        print(i)
        before = Afields_hist[i]
        after = AB_fields_hist[i]
        increase = before - after
        sum+=increase * w
        w=w/1.5

    return sum

def eval_many_hypos_for_descriptor(pics, hypotheses_list, descriptor, nbins):
    evaluations=[]
    for hypo in hypotheses_list:
        evaluation = measure_discrim_power_of_hypo_onto_descr(pics, hypo, descriptor, nbins)
        evaluations.append(evaluation)
    return evaluations

