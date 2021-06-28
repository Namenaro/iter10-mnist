from discriminator import *
from utils import *
from data import *
from checkers import *
from logger import *

# суть эксперимента: для выбранных вручную разынх точек напечатать
# значения их дискриминантной силы при заданном радусе/сайде
def make_experiment(X, Y, side, radius):
    pics = etalons_of3()
    pic = etalons_of3()[0]
    nbins = 10
    parent_x = 5
    parent_y = 16
    descriptor = get_descriptor(pic, x=parent_x, y=parent_y, side=1)
    hypotheses_list = init_hypos_const_side(pic, X,Y, side, radius, parent_x, parent_y)
    evaluations = eval_many_hypos_for_descriptor(pics, hypotheses_list, descriptor, nbins)
    return evaluations


def get_descriptor(pic, x, y, side):
    pics_for_stat = get_diverse_set_of_numbers(20)
    checker = check_mean
    A = init_descriptor(pic, x, y, side, checker, pics_for_stat)
    return A


def init_hypos_const_side(pic, X,Y, side, radius,parent_x, parent_y):
    checker = check_mean
    pics_for_stat = get_diverse_set_of_numbers(20)
    hypotheses_list = []
    for i in range(0, len(X)):
        hypo = init_hypo(side, checker, pics_for_stat, pic, X[i], Y[i], parent_x, parent_y, radius)
        hypotheses_list.append(hypo)
    return hypotheses_list

if __name__ == "__main__":
    logger = HtmlLogger("mean2")
    pic = etalons_of3()[0]
    X,Y = select_coord_on_pic(pic)
    fig = visualise_points_on_fig(pic, X, Y)
    logger.add_fig(fig)
    evals = make_experiment(X,Y, side=2, radius=4)
    logger.add_text(str(X) + ", Y=" + str(Y) )
    logger.add_text("evals: " + str(evals))
    logger.close()

