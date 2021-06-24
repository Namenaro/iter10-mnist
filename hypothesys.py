from clicker import *
from utils import *

class Hypothesys:
    def __init__(self, descriptor, dx, dy, radius):
        self.A = descriptor
        self.dx = dx
        self.dy = dy
        self.radius = radius

    def check_hypothesys(self, pic, x,y):
        expected_x = x + self.dx
        expected_y = y + self.dy

        X, Y = get_coords_less_or_eq_raduis(expected_x, expected_y, self.radius)
        temporary_hypotheses = {}
        for i in range(len(X)):
            alignment = self.A.apply(pic, X[i], Y[i])
            ddx = X[i]-expected_x
            ddy = Y[i]-expected_y

            temporary_hypotheses[(ddx, ddy)] = alignment

        alignment, ddx, ddy = find_best_hypothesys(temporary_hypotheses)
        return alignment, ddx ,ddy

    def apply_to_all_pic(self, pic):
        ymax = pic.shape[0]
        xmax = pic.shape[1]

        res = np.zeros((ymax, xmax))
        for centery in range(0, ymax):
            for centerx in range(0, xmax):
                alignment, ddx ,ddy = self.check_hypothesys(pic, centerx, centery)
                res[centery, centerx] = alignment
        return res



