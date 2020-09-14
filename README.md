# Lane Detection using FCN (VGG-16)
Hi, I am going to build a model to segment road lanes using VGG-16. 

Computer vision is solving various problem in the field of AI, Easing life of industries by solving & easing up the tiresome tasks. Semantic Segmentation is one of the important topic in the field of self-driving. It paves the way towards complete scene of understanding the surroundings. 
Semantic segmentation is widely divided into three steps, Those are Classification, Localization, Finally Semantic segmenation. 

Few standard deep networks that have made significant contribution in the field of Computer Vision are: 

1.) AlexNet 
2.) VGG-16 
3.) GoogLeNet
4.) ResNet 

## Existing Semantic Segmentation Approaches are encoder network followed by a decoder network. 

1.) The encoder is usually is a pre-trained classification network like VGG/ResNet followed by decoder network. 

2.) Decoder projects lower resolution learnt by the encoder onto high resolution to get a dense classification. 

Semantic segmentation (SS) is different from classification task where the end result of very deep network is the only important things, Semantic Segmentation learns feature at different stages of encoder. The three main approaches for employing different mechanism: 

 1.) Region-Based semantic segmentation: RCNN (Regions with CNN feature) It performs the semantic segmentation based on the object detection results.The working od RCNN is like first utilizing selective search to extract a large quantity of object proposals and then computes CNN feature for each of them.CNN are mainly intended for image classification but RCNN can address more complicated task such as object detect ion and image segmentaion. RCNN extracts 2 type of feature for each region: full region feature and foreground feature. 
  Few drawbacks for segmentation task: 
    1. Feature is not compatiable with the segmentation task. 
    2. It does not contain enough spaitail information for precise boundary generation 

 2.) Fully Convolutional Network based semantic segmentation: 
    It learns a mapping from pixel to pixel, without extracting the region proposals. FCN has only pooling and convolutional layers which give them the ability to make predicitions on arbitary-sized inputs. One issue in FCN is that the resolution of the output feature maps is down sampled due to propagating through several alternated convolutional and pooling layer. Hence the preidictions are typically in low resolution, resulting in relatively fuzzy object boundaries.  

     Unlike the convolutional neural networks previously introduced, an FCN transforms the height and width of the intermediate layer feature map back to the size of input image through the transposed convolution layer, so that the predictions have a one-to-one correspondence with input image in spatial dimension (height and width).  

     The fully convolutional network first uses the convolutional neural network to extract image features, then transforms the number of channels into the number of categories through the  1×1  convolution layer, and finally transforms the height and width of the feature map to the size of the input image by using the transposed convolution layer. 

