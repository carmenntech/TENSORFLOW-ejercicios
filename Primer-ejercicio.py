import tensorflow as tf

#para usar tensorflow siempre es  necesario crear un vector
vector = tf.constant([26,28])

with tf.Session() as s:
    print(s.run(vector))

    