import tensorflow as tf
import numpy as np

X_train = (np.random.sample((10000,5)))
y_train = (np.random.sample((10000,1)))

feature_columns = [tf.feature_column.numeric_column('x', shape=X_train.shape[1:])]
DNN_reg = tf.estimator.DNNRegressor(
    feature_columns=feature_columns,
    model_dir='train/linreg',
    hidden_units=[500,300],
    optimizer=tf.train.ProximalAdagradOptimizer(
        learning_rate=0.1,
        l1_regularization_strength=0.001
    )
)

train_input = tf.estimator.inputs.numpy_input_fn(
    x={"x" : X_train},
    y=y_train,
    shuffle=False,
    num_epochs=None
)

DNN_reg.train(input_fn=train_input, steps=3000)
