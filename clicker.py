import matplotlib.pyplot as plt
import math

class CoordSelector:
    def __init__(self, image):
        self.image = image
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.resultx = []
        self.resulty = []

    def onclick(self, event):
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
        x = math.ceil(event.xdata)
        y = math.ceil(event.ydata)
        plt.scatter(x, y, s=100, c='red', marker='o', alpha=0.4)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        self.resultx.append(math.ceil(event.xdata))
        self.resulty.append(math.ceil(event.ydata))


    def create_device(self):
        plt.imshow(self.image, cmap='gray_r')
        plt.show()
        return self.resultx, self.resulty

def select_coord_on_pic(pic):
    devcr = CoordSelector(pic)
    x, y = devcr.create_device()
    return x,y
