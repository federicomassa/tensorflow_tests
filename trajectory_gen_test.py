from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

import numpy as numpy
import matplotlib.pyplot as plt

# Trajectory output length
N = 100

# Number of samples
samples = 1000

dummy_input = np.array(0.0,1.0,2.0,3.0,4.0,5.0)
dummy_output = np.zeros(N)

train_X = np.array([dummy_input for i in range(samples)])
train_y = np.array([dummy_output for i in range(samples)])

# Setup model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(N)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(N, activation='softmax'),
])

# Compile model
model.compile(optimizer='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(train_images, train_labels, epochs=10)

# Test
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

# Predict
predictions = model.predict(test_images)


