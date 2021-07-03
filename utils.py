import operator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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


def show_several_lines_pics_with_one_colorbar(pics_series):
    rows = len(pics_series)
    num_pics_in_seria = len(pics_series[0])
    fig, axs = plt.subplots(rows, num_pics_in_seria)
    MIN, MAX = np.array(pics_series).min(), np.array(pics_series).max()
    for row in range(rows):
        for col in range(num_pics_in_seria):
            im = axs[row, col].imshow(pics_series[row][col], cmap='Blues', vmin=MIN, vmax=MAX)

    fig.colorbar(im, ax=axs.ravel().tolist())
    return fig

def visualise_points_on_fig(pic, X,Y):
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    plt.scatter(X[0], Y[0], s=100, c='red', marker='o', alpha=0.4)
    plt.scatter(X[1:], Y[1:], s=100, c='green', marker='o', alpha=0.4)
    return fig

def visualise_graphs(graphs, names):
    fig, axs = plt.subplots(len(graphs))
    for i in range(len(graphs)):
        axs[i].plot(graphs[i])
        axs[i].set_title(names[i])

    return fig


def get_many_XY():
    X = [5, 7, 8, 9, 11, 10, 12, 13, 14, 13, 14, 17, 17, 16, 14, 13, 14, 16, 16, 16, 15, 14, 13, 12, 14, 16, 17, 18, 19,
         19, 19, 18, 17, 16, 15, 15, 17, 19, 21, 20, 19, 18, 16, 15, 14, 13, 11, 12, 14, 15, 16, 14, 13, 11, 10, 10, 11,
         8, 9, 12, 15, 17, 20, 21, 22, 22, 21, 20, 19, 17, 16, 18, 19, 20, 20, 19, 18, 17, 17, 17, 16, 15, 14, 13, 11,
         11, 9, 11, 10, 10, 12, 13, 13, 12, 11, 12, 10, 7, 7, 5, 2, 1, 5, 4, 5, 6, 5, 4, 4, 4, 7, 3, 6, 15, 16, 15, 15,
         6, 6, 7, 8, 8, 7, 9, 10, 12, 12, 13, 13, 12, 10, 9, 8, 6, 5, 4, 2, 4, 6, 9, 11, 14, 16, 19, 21, 21, 21, 21, 20,
         23, 23, 20, 18, 12, 9, 13, 12, 15, 15, 15, 14, 13, 12, 12, 18, 18, 16, 14, 12, 13, 11, 16, 17, 20, 18, 18, 20,
         19, 18, 19, 16, 18, 18, 16, 15, 15, 15, 14, 15, 11, 11, 10, 12, 10, 8, 5, 4, 3, 3, 3, 3, 7, 7, 6, 4, 5, 5, 6,
         13, 13, 12, 9, 12, 9, 9, 12, 11, 9, 14, 16, 18, 17, 17, 17, 16, 18, 20, 20, 19, 20, 21, 19, 11, 17, 15, 14, 14,
         13, 11, 8, 5, 3, 4, 6, 7, 6, 11, 21, 22, 21, 18, 18, 17, 16, 13, 11, 9]
    Y = [17, 17, 18, 19, 20, 20, 19, 18, 16, 16, 15, 15, 17, 17, 18, 20, 20, 19, 18, 16, 14, 13, 14, 12, 12, 11, 12, 13,
         14, 15, 17, 16, 14, 13, 12, 11, 10, 11, 11, 9, 9, 8, 8, 9, 10, 10, 7, 8, 8, 7, 6, 5, 5, 5, 6, 7, 8, 7, 5, 3, 3,
         3, 3, 4, 6, 9, 7, 5, 4, 5, 4, 5, 6, 6, 8, 7, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 13, 14, 13, 12,
         13, 16, 14, 18, 15, 11, 7, 15, 19, 14, 11, 18, 19, 20, 19, 18, 17, 17, 17, 17, 17, 15, 16, 15, 20, 22, 21, 20,
         21, 23, 23, 22, 22, 23, 23, 21, 21, 21, 22, 22, 21, 21, 21, 20, 23, 24, 25, 25, 24, 23, 21, 19, 16, 15, 13, 12,
         7, 4, 2, 1, 1, 2, 7, 5, 4, 5, 6, 7, 6, 6, 7, 4, 3, 3, 4, 4, 4, 4, 7, 9, 10, 10, 9, 7, 8, 7, 5, 5, 18, 20, 20,
         20, 19, 21, 21, 23, 22, 21, 23, 24, 24, 24, 23, 22, 21, 20, 19, 18, 19, 18, 18, 20, 19, 22, 23, 20, 19, 20, 20,
         18, 16, 11, 9, 9, 9, 2, 1, 19, 18, 20, 19, 21, 23, 19, 13, 12, 16, 18, 18, 19, 22, 22, 22, 23, 25, 27, 26, 25,
         23, 16, 16, 13, 9, 11, 8, 6, 6, 15, 14, 13, 12, 22, 23, 21]
    return X, Y

def draw_hypos(hypos, pic, parentx, parenty ):
    X=[]
    Y=[]
    c=[]
    k=0
    for hypo in hypos:
        X.append(hypo.dx +parentx)
        Y.append(hypo.dy + parenty)
        c.append(k)
        k+=1
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    plt.scatter(X, Y, s=100, c=c, marker='o', alpha=0.4, cmap='inferno')
    plt.colorbar()
    return fig

def show_several_pics_with_one_colorbar(seria):
    rows = 2
    num_pics_in_seria = len(seria)
    fig, axs = plt.subplots(rows, num_pics_in_seria)
    MIN, MAX = np.array(seria).min(), np.array(seria).max()

    for col in range(num_pics_in_seria):
        im = axs[0, col].imshow(seria[col], cmap='Blues', vmin=MIN, vmax=MAX)

    fig.colorbar(im, ax=axs.ravel().tolist())
    return fig
