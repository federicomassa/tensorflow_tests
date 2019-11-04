from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

import numpy as numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print("TF Version: ", tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['t-shirt','trouser','pullover','dress','coat','sandal','shirt','sneaker','bag','boot']

train_images = train_images/255.0
test_images = test_images/255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])

plt.show()

# Setup model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax'),
])

# Compile model
model.compile(optimizer='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("Shape:", train_images.shape, train_labels.shape)
print("Summary:", model.summary())

model.fit(train_images, train_labels, epochs=10)

# Test
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

# Predict
predictions = model.predict(test_images)


