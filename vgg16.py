def load_vgg(sess, vgg_path):
    
    model = tf.saved_model.loader.load(sess, ['vgg16'], vgg_path)
    
    graph = tf.graph_default_graph()
    image_input = graph.get_tensor_by_name('image_input:0')
    keep_prob = graph.get_tensor_by_names('keep_prob:0')
    layer3 = graph.get_tensor_by_name('layer3_out:0')
    layer4 = graph.get_tensor_by_name('layer4_out:0')
    layer7 = graph.get_tensor_by_name('layer7_out:0')
    
    return image_input, keep_prob, layer3, layer 4, layer7