
# Object Segmentation and Rotation Using Mask R-CNN

A tool that uses Mask R-CNN to segment objects in images and rotate them based on user-specified angles, while preserving the original background. This project implements object segmentation and rotation using the **Mask R-CNN** model. The primary objective is to detect and manipulate the pose of objects in images, specifically focusing on chairs in this implementation.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [License](#license)

## Installation

To run this project, ensure you have **Python 3.x** installed. Follow the steps below to set up the environment and install the necessary dependencies:

1. Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Install necessary packages: Install TensorFlow and OpenCV for image processing:
   ```bash
   pip install tensorflow opencv-python
4. Download and extract the Mask R-CNN model: You need the Mask R-CNN pre-trained model from TensorFlow's model zoo. Run the following commands to download and extract the model:
   ```bash
   wget -O mask_rcnn_inception_v2_coco_2018_01_28.tar.gz http://download.tensorflow.org/models/mask_rcnn_inception_v2_coco_2018_01_28.tar.gz
   tar -xvf mask_rcnn_inception_v2_coco_2018_01_28.tar.gz
   
## Usage

To run the segmentation and rotation of an object, use the following command:

```python3 cli.py --image "/Users/sahilnarwal/Desktop/Ayush/images_Of_Chair.jpeg" --class_name "chair" --azimuth 45 --output "/Users/sahilnarwal/Desktop/Ayush/output_image.jpg"```

## How It Works

1. Image Loading: The input image is loaded using OpenCV.
2. Model Loading: The Mask R-CNN model is loaded using TensorFlow.
3. Object Segmentation: The model processes the image and detects objects based on the specified class name (e.g., "chair").
4. Object Rotation: The detected objects are rotated according to the specified azimuth angle, while the background remains intact.
5. Output: The final image, with the rotated object, is saved to the specified output path.

## Input
![Output Image](https://github.com/Ayush-chanchal/Object-Segmentation-and-Rotation-Using-Mask-R-CNN/blob/main/images_Of_Chair.jpeg "Rotated Object Output")

