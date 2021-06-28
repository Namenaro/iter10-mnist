from discriminator import *
from utils import *
from data import *
from checkers import *
from logger import *

# суть эксперимента: для выбранных вручную разынх точек напечатать
# значения их дискриминантной силы при заданном радусе/сайде
def make_experiment(X, Y, side, radius):
    pics = get_numbers_of_type(3)[0:10]
    #pics = etalons_of3()
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

def visualise_evals_at_fig(X,Y,list_of_evals, pic_shape):
    num_pics = len(list_of_evals)
    cm = plt.cm.get_cmap('RdYlBu')
    max, min = np.array(list_of_evals).max(),np.array(list_of_evals).min()
    if min>0:
        min=0
    fig, ax = plt.subplots(num_pics)
    for i in range(num_pics):
        res = np.zeros(pic_shape)
        evals = list_of_evals[i]
        ax[i].imshow(res, cmap='gray_r')
        sc = ax[i].scatter(X, Y, s=100, c=evals, marker='o', vmax=max, vmin=min, alpha=0.4, cmap=cm)
    plt.colorbar(sc)
    return fig

if __name__ == "__main__":
    logger = HtmlLogger("mean2")
    pic = etalons_of3()[0]
    X,Y = select_coord_on_pic(pic)
    fig = visualise_points_on_fig(pic, X, Y)
    logger.add_fig(fig)
    list_of_evals=[]

    radius = 4
    logger.add_text("radius = "+ str(radius))
    evals1 = make_experiment(X,Y, side=2, radius=radius)
    logger.add_text(str(X) + ", Y=" + str(Y) )
    logger.add_text("evals: " + str(evals1))
    list_of_evals.append(evals1)

    radius = 2
    logger.add_text("radius = " + str(radius))
    evals2 = make_experiment(X, Y, side=2, radius=radius)
    logger.add_text(str(X) + ", Y=" + str(Y))
    logger.add_text("evals: " + str(evals2))
    list_of_evals.append(evals2)


    radius = 1
    logger.add_text("radius = " + str(radius))
    evals3 = make_experiment(X, Y, side=2, radius=radius)
    logger.add_text(str(X) + ", Y=" + str(Y))
    logger.add_text("evals: " + str(evals3))
    list_of_evals.append(evals3)


    fig = visualise_evals_at_fig(X, Y, list_of_evals, pic.shape)
    logger.add_fig(fig)

    logger.close()

