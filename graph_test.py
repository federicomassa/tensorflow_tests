import tensorflow as tf

x = tf.get_variable("x", dtype=tf.int32, initializer=tf.constant([5]))
z = tf.get_variable("z", dtype=tf.int32, initializer=tf.constant([6]))
c = tf.constant([5], name="constant")
square = tf.constant([2], name="square")

f = tf.multiply(x,z) + tf.pow(x, square) + z + c

init = tf.global_variables_initializer()

with tf.Session() as sess:
    init.run()
    function_result = f.eval()
    
print(function_result)
