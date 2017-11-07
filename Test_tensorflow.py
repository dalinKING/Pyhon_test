import tensorflow as tf

hello=tf.constant("heloo tensorflow!")

sess=tf.Session()

print(sess.run(hello))