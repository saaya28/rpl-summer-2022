# Requirements:
* Shapes
* Location
* Size
* Color (not necessary)
## YOLO:
YOLO is extremely fast (45 frames per second) than other object detection algorithms because it uses frame detection as a regression problem so we do not need a complex pipeline. It reasons globally about the image when making predictions and sees the entire image during training and test time. It also learns generalizable representations of objects. 

One drawback is that it lags behind state-of-the-art detection systems in accuracy. This shouldn’t be a major problem because we do not want to measure anything but just detect the pipette. Another drawback is that struggles with small objects within the image because of the spatial constraint of the algorithm. This will be a problem for us if we choose to detect residues in the pipette.  

## RCNN? 
RCNN takes a huge amount of time and cannot be implemented in real time. Also, the search algorithm is fixed so there’s no learning there. 

https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e 
