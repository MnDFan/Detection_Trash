Detection of material

The main goal of this project is to explore the fundamentals of autonomous image
recognition using various algorithms and computer vision models. It also aims to
develop a sample recognition model by training it with data sourced from Google
Images or other popular web-based image search engines.

During this project, we will use YOLOv5 (You Only Look Once) which is an algorithm
capable of detecting objects in real-time by performing detection and classification
simultaneously. YOLO has been widely evaluated and offers a solid approach to basic
tasks such as classification, detection, segmentation, and tracking. Initially a concept,
it has since been implemented by many developers. One of its key advantages is its
relatively lightweight nature, allowing it to run on most modern desktop hardware
without requiring an internet connection. The objective is to sort different objects like a
plastic bottle, cup of glasses or a sachet for example. First, we need to be able to
recognize these different objects on the video to be able to sort them. After that, the
algorithm should be able to detect the type of object. Our expectation with this project
is we hope to be use in a real project for more action to decrease the pollution in the
world.

Performance metrics

*Different YOLO model

*Result

Yolov11 nano for 100 epochs:

Global metrics:

![results](https://github.com/user-attachments/assets/4b250e63-f588-4046-a2d5-c0b9289cd016)

Prediction for the validation set:

![val_batch2_pred](https://github.com/user-attachments/assets/e37eb06d-577b-4a38-9580-434b8c5923c2)



Yolov11 medium for 100 epochs:

Global metrics:

![results](https://github.com/user-attachments/assets/b8fd690f-24cc-4726-bd56-64cdf3d7f953)

Prediction for the validation set:

![val_batch2_pred](https://github.com/user-attachments/assets/44a4cc27-4466-4246-b8fe-8f8e0669f2a3)

