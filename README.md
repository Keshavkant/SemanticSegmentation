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

 1.) Region-Based semantic segmentation: RCNN (Regions with CNN feature) It performs the semantic segmentation based on the object detection results.The working od RCNN is like first utilizing selective search to extract a large quantity of object proposals and then computes CNN feature for each of them.CNN are mainly intended for image classification but RCNN can address more complicated task such as object detection and image segmentaion. 

 2.)    
