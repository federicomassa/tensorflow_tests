import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib import lines
import numpy as np

L1 = 20.0
w = 10.0
R1 = 30.0
R11 = R1 - w/2.0
R12 = R1 + w/2.0
alpha = 30
L2 = 100.0
dt = 0.1
samples = 20
a_max = 10
omega_max = 1

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


def model(init, controls):
    traj = [None]*len(controls)
    traj[0] = Point(init.x, init.y, init.theta, init.v)

    for i in range(1, len(traj)):
        traj[i] = Point()
        traj[i].x = traj[i-1].x + traj[i-1].v*np.cos(traj[i-1].theta)*dt
        traj[i].y = traj[i-1].y + traj[i-1].v*np.sin(traj[i-1].theta)*dt
        traj[i].theta = traj[i-1].theta + controls[i-1].omega*dt
        traj[i].v = traj[i-1].v + controls[i-1].a*dt

    return traj

fig = plt.figure()
ax = plt.gca()
ax.axis('equal')
ax.axis([0, 200, -100, 100])

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


sample_controls = [Control((np.random.rand()-0.5)*2*a_max, (np.random.rand()-0.5)*2*omega_max) for i in range(samples)]
init_state = Point(0.0,0.0,0.0,20.0)

traj = model(init_state, sample_controls)

#for i in range(len(traj)):
#    print(traj[i].x, traj[i].y)

traj_x = [traj[i].x for i in range(len(traj))]
traj_y = [traj[i].y for i in range(len(traj))]

plt.plot(traj_x, traj_y, 'r-o')

plt.show()
