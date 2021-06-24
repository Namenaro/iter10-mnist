import operator
import numpy as np
import matplotlib.pyplot as plt

def get_sensory_array(pic, centerx, centery, radius):
    XB, YB = get_coords_less_or_eq_raduis(centerx, centery, radius)
    return get_sensory_array_by_coords(pic, XB, YB)

def get_sensory_array_by_coords(pic, XB, YB):
    arr = []
    for i in range(len(XB)):
        x=XB[i]
        y=YB[i]
        xlen = pic.shape[1]
        ylen = pic.shape[0]
        if x >= 0 and y >= 0 and x < xlen and y < ylen:
            arr.append(pic[y,x])
        else:
            arr.append(0)
    return np.array(arr)


def get_coords_less_or_eq_raduis(centerx, centery, radius):
    XB = []
    YB = []
    for r in range(0, radius+1):
        X, Y = get_coords_for_radius(centerx, centery, r)
        XB = XB + X
        YB = YB + Y
    return XB, YB

def get_coords_for_radius(centerx, centery, radius):
    #x+y=radius ->  y=radius-x
    X=[]
    Y=[]
    for x in range(0,radius+1):
        y=radius-x
        X.append(x+centerx)
        Y.append(y+centery)
    return X,Y

def find_best_hypothesys(dict_hypotheses):
    sorted_hypos = sorted(dict_hypotheses.items(), key=operator.itemgetter(1),reverse=True)
    best_hypo = sorted_hypos[0]
    dxdy= best_hypo[0]
    val = best_hypo[1]
    return val, dxdy[0], dxdy[1]


def show_several_pics_with_one_colorbar(pics):
    rows = 2
    fig, axs = plt.subplots(rows, len(pics))
    MIN, MAX = np.array(pics).min(), np.array(pics).max()
    for i in range(len(pics)):
        im = axs[0, i].imshow(pics[i], cmap='Blues', vmin=MIN, vmax=MAX)

    fig.colorbar(im, ax=axs.ravel().tolist())
    return fig

def visualise_points_on_fig(pic, X,Y):
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    plt.scatter(X[0], Y[0], s=100, c='red', marker='o', alpha=0.4)
    plt.scatter(X[1:], Y[1:], s=100, c='green', marker='o', alpha=0.4)
    return fig

