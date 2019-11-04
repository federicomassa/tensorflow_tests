from draw_track import draw_track
from draw_track import Control
from draw_track import Point
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

dt = 0.1
samples = 10000
iterations = 20
a_max = 10
omega_max = 1

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


if __name__=='__main__':

    draw_track(20, 6, 10, 30, 50)

    # Setup model
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(7,)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense((iterations*2), activation='linear')
    ])

    # Compile model
    model.compile(optimizer='adam',
        loss = 'mean_squared_error',
        metrics=['mae']
    )

    # Generation of y: TODO replace this with real data
    y = np.empty((samples, iterations*2))
    for i in range(samples):
        sample_controls = [None]*iterations*2

        # For each iteration
        for j in range(iterations):
            sample_controls[j] = (0.6-0.5)*2*a_max

        for j in range(iterations, iterations*2):
            sample_controls[j] = (0.4-0.5)*2*omega_max

        y[i] = sample_controls

    # Normalize output data
    y_norm = np.empty(y.shape)

    for i in range(y.shape[0]):
        for j in range(len(y[i])):
            if j < len(y[i])/2.0:
                y_norm[i][j] = y[i][j]/(2*a_max) + 0.5
            else:
                y_norm[i][j] = y[i][j]/(2*omega_max) + 0.5

    # Generation of X
    X = np.empty((samples,7))
    for i in range(samples):
        X[i] = [np.random.rand(),np.random.rand(),np.random.rand(),np.random.rand(),np.random.rand(),np.random.rand(),np.random.rand()]

    print("X,y:",X.shape, y_norm.shape)        
    print(model.summary())

    predictions = model.predict(X)
    print(predictions)
    model.fit(X, y_norm, epochs=10)

    predictions = model.predict(X)
    print(predictions[0])

    # init_state = Point(0.0,0.0,0.0,20.0)

    # traj = model(init_state, sample_controls)

    # #for i in range(len(traj)):
    # #    print(traj[i].x, traj[i].y)

    # traj_x = [traj[i].x for i in range(len(traj))]
    # traj_y = [traj[i].y for i in range(len(traj))]

    # plt.plot(traj_x, traj_y, 'r-o')

    # plt.show()