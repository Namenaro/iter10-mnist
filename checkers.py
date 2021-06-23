import numpy as np

def check_dispersion(sensory_array):
    return np.var(sensory_array)

def check_mean(sensory_array):
    return np.mean(sensory_array)

def check_perepad(sensory_array):
    min = np.min(sensory_array)
    max = np.max(sensory_array)
    span = abs(max - min)
    return span