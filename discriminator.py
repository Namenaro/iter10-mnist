from A import *
from hypothesys import *

def measure_discrim_power_of_hypo_onto_descr(pics, hypothesys, descriptor, nbins):
    Afields = []
    ABfields = []
    for pic in pics:
        Afield = descriptor.apply_to_pic(pic)
        Bfield = hypothesys.apply_to_all_pic(pic)
        ABfield = Afield+Bfield
        Afields = Afields + Afield.flatten().tolist()
        ABfields = ABfields + ABfield.flatten().tolist()
    Afields_hist = get_gist(Afields, 1, nbins)
    AB_fields_hist = get_gist(ABfields, 2, nbins)
    discrim_power = measure_entropy_decrease(Afields_hist, AB_fields_hist)
    return discrim_power



def measure_entropy_decrease(Afields_hist, AB_fields_hist):
    pass