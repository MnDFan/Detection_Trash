#Detection of material

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

Installation and Usage 

Code on this project
- train.py is use train dataset on parameters
- detect_custom to launch the code on a image to detect object base on the training of a dataset ( you will see 2 detect_custom, the first one is base on the nano model and the second one is base on the medium model)

Before starting to train any dataset, you will need to install:
- Ultralytics
- CUDA toolkit 
- Pytorch 

For this project we hqve use:
- Ultalytics 
- Torch 2.5.1+cu118
- CUDA 11.8


Performance metrics

*Different YOLO model
The original dataset was created by collecting images from online sources such as Google Images and others. Some of these images may be subject to copyright protection. Labeling was performed using Roboflow, and the dataset was split as follows: 97% for the training set, 3% for the validation set, and 1% for the test set. Although the validation set could have been larger, the limited number of images led to prioritizing the accuracy of the training phase.

For the training on the dataset, we use a RTX Nvidia 3060 Laptop GPU. Firstly we had use the nano medium that took 1 hour to complete the training for 100 epochs. After that, we try we the same set the medium and it took a really long time : 12 hours to complete the training dataset. However we will see in the next result if it was worth it.

Yolov11 nano for 100 epochs:

Global metrics:

![results](https://github.com/user-attachments/assets/4b250e63-f588-4046-a2d5-c0b9289cd016)

Prediction for the validation set:

![val_batch2_pred](https://github.com/user-attachments/assets/e37eb06d-577b-4a38-9580-434b8c5923c2)



Yolov11 medium for 100 epochs:

Global metrics:

![results](https://github.com/user-attachments/assets/b8fd690f-24cc-4726-bd56-64cdf3d7f953)

Prediction for the validation set:

![val_batch0_pred](https://github.com/user-attachments/assets/a361b586-cba7-45b7-bf11-aae5053a2159)

At first sight, we can think that these two model is the same, but with long term the medium model will be a better use to recognize some object in the picture.

There is some result we test on the medium model:

![7](https://github.com/user-attachments/assets/4e8794c4-ff09-40f2-b60e-913fcdd5f653)

but here we can see some error during the detection phase like he can't really separate object:

![6](https://github.com/user-attachments/assets/c8512910-6951-449f-91c2-6e167c650b40)

The problem should be the difficulty to have a good dataset every trash that could exist. there is a lot of different object and so to train with.

Future work:

For the future work, we can for example add more classe to let the programme have more object to detect in a image

![labels](https://github.com/user-attachments/assets/9df23bfd-489d-4664-8695-04be4e068f94)

Use a better GPU and model to not waste some time and to train again and again foor nothing.

Issues and Contributions

For now, you could use a better dataset and a better YOLO model for example. Don't hesitate to add this project to your repository to add some improvement, i will be more than happy.

Reference

  - Ultralytics
  - YOLO11 Github
  - Roboflow Website
  - Pytorch Website
  - CUDA Website




