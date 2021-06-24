# цель эксперимента: показать групповой эффект многих Б на "осветление" невязки избранного А.
# А именно, нужно показать, что чем больше опорных точек Б, тем светлее истинная точка А.
# Радиусы назначим волюнтаристски. Частоту встречания бешек и ашки пока учитывать не будем,
# речь идет только про невязку.

from utils import *
from clicker import *
from data import *
from checkers import *
from hypothesys import *
from A import *
from logger import *


def make_experiment(pic, X, Y, side, radius, checker):
    A, hypotheses = init_A_and_all_hypos(pic, side, radius, checker, X, Y)
    return visualise_A_and_hypos(A, hypotheses, pic)


def init_A_and_all_hypos(pic, side, radius, checker, X, Y):
    pics_for_stat = get_diverse_set_of_numbers(20)
    A = init_descriptor(pic, X[0], Y[0], side, checker, pics_for_stat)
    hypotheses_list = []
    for i in range(1, len(X)):
        descriptor = init_descriptor(pic, X[i], Y[i], side, checker, pics_for_stat)
        dx = X[i] - X[0]
        dy = Y[i] - Y[0]
        hypo = Hypothesys(descriptor, dx, dy, radius)
        hypotheses_list.append(hypo)

    return A, hypotheses_list


def visualise_A_and_hypos(A, hypotheses_list, pic):
    pics = [A.apply_to_pic(pic)]
    for i in range(len(hypotheses_list)):
        print("hypo " + str(i) + "...")
        new_pic = hypotheses_list[i].apply_to_all_pic(pic)
        new_pic = new_pic + pics[i]
        pics.append(new_pic)

    fig = show_several_pics_with_one_colorbar(pics)
    return fig



if __name__ == "__main__":
    logger = HtmlLogger("mean")
    checker = check_mean
    pic = etalons_of3()[0]
    X, Y = select_coord_on_pic(pic)
    fig =visualise_points_on_fig(pic, X,Y)
    logger.add_fig(fig)

    side = 1
    radius = 6
    logger.add_text("side" + str(side) + "_radius" + str(radius))
    fig = make_experiment(pic, X, Y, side, radius, checker)
    logger.add_fig(fig)


    side = 1
    radius = 4
    logger.add_text("side"+str(side)+"_radius"+str(radius))
    fig = make_experiment(pic, X, Y, side, radius, checker)
    logger.add_fig(fig)

    side = 1
    radius = 1
    logger.add_text("side" + str(side) + "_radius" + str(radius))
    fig = make_experiment(pic, X, Y, side, radius, checker)
    logger.add_fig(fig)


    logger.close()
