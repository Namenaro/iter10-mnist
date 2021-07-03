from scipy.special import softmax
import numpy as np

from utils import *
from clicker import *
from data import *
from checkers import *
from hypothesys import *
from A import *
from logger import *

def informativness_of_field_of_descr(field):
    max = max(field)
    sfield = softmax(field)
    mfield = field/max



