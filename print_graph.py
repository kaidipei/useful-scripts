import tensorflow as tf
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file

meta_model_file = 'file name here'

print_tensors_in_checkpoint_file(file_name=meta_model_file, tensor_name = '', all_tensors = True, \
                          all_tensor_names=False)

checkpoint = tf.train.get_checkpoint_state(meta_model_file)

with tf.Session() as sess:
    for var_name, _ in tf.contrib.framework.list_variables(meta_model_file):

        print(var_name)