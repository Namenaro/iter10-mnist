# берем данную точку, генерим из нее дескриптор А, и считаем поле А на эталоне.

# из эталона генерим кучу гипотез, и для них считаем их поля
# (при создании гипотез выбираем нулевой радиус и минимальный сайд).

# передаем поле А  и поля гипотез в функцию, которая ищет среди полей гипотез
# лучшее в смысле его взаимодействия с полем А

# когда гпотеза В с лучшим полем найдена, мы рассчитываем новое поле АВ
# оцениваем его "хорошесть" - поле максимально хорошо тогда, когда максимум один (максимаьная дискриминация)
# и максимально плохо тогда, когда явркость во всех точках одинаковая (минимальная дискриминация точек).
# Если нормировать поле к единице, то можно рассмотреть энтропию от его значений. И ее значение на поле
# АВ эталона можно считать за хорошесть поля. Помимо дискриминативных свойств поля, можно в оценку хорошести
# включить высоту максимума.

# дальше процесс повторяется рекурсивно: новое поле АВ на второй итерации будет заместо поля А. Поля
# гипотез мы опять рассмариваем все те же, что раньше, только исключив их списка поле В, так как
# его уже рассмотрели. На каждом шаге рекурсии получаем новое поле и для него оценку хорошести.

# Этот ряд хорошестей можно нарисовать ,и ожидается, что график получится ыстро убывающий и выходящий на плато.
# Точка выхода на плато определяет необходимый минимум управлений, достаточных для идентификации исходной точки А.
# Высота плато- в свою очеередь даем нам потенцияал улучшаемости поля А за счет вхаимодействия с другими полями.

# задача в целом состоит в том, чтоб найти топ точек (А1, А2, ...) которые можно идентифицировать с наилучшей точностью
# за наименьшее количество управлений. Желательно, чтоб это было устойчиво по отношению к радиусу. Выживаемость

# ЭТАП 2- это переносимость точек (А1, А2, ...) между набором эталонов. Задача в том,
# чтобы каждая точка "срабатывала" на каждом эталоне. Для каждой точки нам ока известны лишь гипотезы,
# и порядок их применения, но их параметры надо перенастроить: изменить радиус. Именно, надо
# постепенно увеличивать его до тех пор, пока точка не сработает на всех эталонах. Если поставить радиус
# слишком большой, то точка сработает на всех картинках не только эталонах. Поэтому нужен такой радиус, что,
# с одной строны, гипотеза выполняется на всех эталонах, а с другой, выполнение гипотезы при таком радиусе
# все еще остается редким событием.

# ЭТАП 3 - Из сработавшей точки деаем предсказания о следующей точке или просто пытаемся предсказать
# что угодно: выбираем наугад управление и выбираем сайд/радиус предсказания так, чтоб оно сбаывалось
# с заданной вероятностью.


from scipy.special import softmax
from scipy.stats import entropy
import numpy as np
import math
from numpy import linalg as LA

from utils import *
from clicker import *
from data import *
from checkers import *
from hypothesys import *
from A import *
from logger import *


def eval_field_discriminativity(field):
    field = field / LA.norm(field)
    ent = entropy(field.flatten())
    return ent


def eval_reduction_of_fieldA_by_fieldB(fieldA, fieldB):  # чем больше тем лучше
    #AB = make_new_field(fieldA, fieldB)
    #return - eval_field_discriminativity(AB)
    return -((make_new_field(fieldA,fieldB)).sum())


def make_new_field(fieldA, fieldB):
    # sfield = softmax(field)
    ones = np.ones_like(fieldA)
    new_field = fieldA * fieldB

    return new_field


def find_best_field(fieldA, fieldsB, excluded_indexes):
    best_red = -math.inf
    best_field_i = None
    for i in range(len(fieldsB)):
        if i not in excluded_indexes:
            red = eval_reduction_of_fieldA_by_fieldB(fieldA, fieldsB[i])
            if red > best_red:
                best_red = red
                best_field_i = i
    return best_field_i, best_red


def range_top_fields(fieldA, fieldsB, num_top_fileds):
    ranged_top_indexes = []
    reductions = []

    current_field = fieldA
    discriminativities = [eval_field_discriminativity(fieldA)]
    for _ in range(num_top_fileds):
        best_field_index, best_reduction = find_best_field(current_field, fieldsB, ranged_top_indexes)
        fieldB = fieldsB[best_field_index]
        current_field = make_new_field(current_field, fieldB)

        ranged_top_indexes.append(best_field_index)
        reductions.append(best_reduction)
        discriminativities.append(eval_field_discriminativity(current_field))
    return ranged_top_indexes, reductions, discriminativities


def get_fields_for_hypos(hypos_list, etalon):
    fields = []
    for hypo in hypos_list:
        field = hypo.apply_to_all_pic(etalon)
        fields.append(field)
    return fields


def get_n_top_hypos_for_descriptor(descr, hypos_list, etalon, num_top_hypos):
    fieldA = descr.apply_to_pic(etalon)

    fieldsB = get_fields_for_hypos(hypos_list, etalon)
    ranged_top_indexes, reductions, discriminativities = range_top_fields(fieldA, fieldsB, num_top_hypos)
    top_hypos=[]
    for i in ranged_top_indexes:
        top_hypos.append(hypos_list[i])
    return top_hypos, reductions, discriminativities


def init_my_descriptor():
    checker = check_mean
    pic = etalons_of3()[0]
    X, Y = select_coord_on_pic(pic)
    side = 1
    pics_for_stat = etalons_of3()[0:20]
    x, y = X[0], Y[0]
    A = init_descriptor(pic, x, y, side, checker, pics_for_stat)
    return A, x, y


def init_hypos(side, radius, X, Y, x_parent, y_parent):
    pics_for_stat = etalons_of3()[0:20]
    checker = check_mean
    pic = etalons_of3()[0]
    hypotheses_list = []
    for i in range(1, len(X)):
        descriptor = init_descriptor(pic, x_parent, y_parent, side, checker, pics_for_stat)
        dx = X[i] - x_parent
        dy = Y[i] - y_parent
        hypo = Hypothesys(descriptor, dx, dy, radius)
        hypotheses_list.append(hypo)

    return hypotheses_list

def get_hypos_seq_fields(pic, descr, hypos):
    fieldA = descr.apply_to_pic(pic)

    fields = [fieldA]
    interfields=[]
    i=0
    for hypo in hypos:
        field_of_hypo = hypo.apply_to_all_pic(pic)
        interfield = make_new_field(fields[i], field_of_hypo)
        fields.append(interfield)
        interfields.append(field_of_hypo)

        i+=1
    return fields, interfields

def make_experiment(side, radius, logger, pic, X, Y, x_parent, y_parent,descr):
    hypos = init_hypos(side, radius, X, Y, x_parent, y_parent)
    top_hypos, reductions, discriminativities = \
        get_n_top_hypos_for_descriptor(descr, hypos, pic, num_top_hypos=3)
    fig = visualise_graphs(graphs=[reductions, discriminativities], names=["reductions", "discriminativities"])
    logger.add_fig(fig)

    fig = draw_hypos(top_hypos, pic, x_parent, y_parent)
    logger.add_fig(fig)

    filds, interfields = get_hypos_seq_fields(pic, descr, top_hypos)
    fig = show_several_pics_with_one_colorbar(filds)
    logger.add_fig(fig)

    logger.add_text("interfields:")
    fig = show_several_pics_with_one_colorbar(interfields)
    logger.add_fig(fig)

if __name__ == "__main__":
    logger = HtmlLogger("mean")

    pic = etalons_of3()[0]

    descr, x_parent, y_parent = init_my_descriptor()
    fig = visualise_points_on_fig(pic, [x_parent], [y_parent])
    logger.add_fig(fig)
    X, Y = get_many_XY()


    side = 2
    radius = 2
    make_experiment(side, radius, logger, pic, X, Y, x_parent, y_parent, descr)


    logger.close()
