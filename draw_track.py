import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib import lines
import numpy as np

class Point:
    def __init__(self, x=None, y=None, theta=None, v=None):
        self.x = x
        self.y = y
        self.theta = theta
        self.v = v

class Control:
    def __init__(self, a=None, omega=None):
        self.a = a
        self.omega = omega

def draw_track(L1, w, R1, alpha, L2):
    plt.figure()
    ax = plt.gca()
    ax.axis('equal')
    ax.axis([0, 200, -100, 100])

    R11 = R1 - w/2.0
    R12 = R1 + w/2.0

    straight11 = lines.Line2D([0.0,L1], [w/2.0,w/2.0], color='black',linewidth=2)
    straight12 = lines.Line2D([0.0,L1], [-w/2.0,-w/2.0],color='black',linewidth=2)
    int_edge1 = patches.Arc((L1,R1), 2*(R11), 2*(R11), 270.0, 0.0, alpha,linewidth=2)
    ext_edge1 = patches.Arc((L1,R1), 2*(R12), 2*(R12), 270.0, 0.0, alpha,linewidth=2)

    x21_min = L1+2*(R11)*np.sin(np.deg2rad(alpha/2.0))*np.cos(np.deg2rad(alpha/2.0))
    x21_max = x21_min + L2*np.cos(np.deg2rad(alpha))
    y21_min = w/2.0 + 2*R11*np.square(np.sin(np.deg2rad(alpha/2.0)))
    y21_max = y21_min + L2*np.sin(np.deg2rad(alpha))

    x22_min = L1+2*(R12)*np.sin(np.deg2rad(alpha/2.0))*np.cos(np.deg2rad(alpha/2.0))
    x22_max = x22_min + L2*np.cos(np.deg2rad(alpha))
    y22_min = -w/2.0 + 2*R12*np.square(np.sin(np.deg2rad(alpha/2.0)))
    y22_max = y22_min + L2*np.sin(np.deg2rad(alpha))

    straight21 = lines.Line2D([x21_min, x21_max], [y21_min, y21_max], color='black',linewidth=2)
    straight22 = lines.Line2D([x22_min, x22_max], [y22_min, y22_max], color='black',linewidth=2)

    ax.add_line(straight11)
    ax.add_line(straight12)
    ax.add_patch(int_edge1)
    ax.add_patch(ext_edge1)
    ax.add_line(straight21)
    ax.add_line(straight22)



if __name__=='__main__':
    draw_track(20, 6, 10, 30, 50)



