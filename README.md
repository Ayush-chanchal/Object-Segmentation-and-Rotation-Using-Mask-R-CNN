
# Object Segmentation and Rotation Using Mask R-CNN

A tool that uses Mask R-CNN to segment objects in images and rotate them based on user-specified angles, while preserving the original background. This project implements object segmentation and rotation using the **Mask R-CNN** model. The primary objective is to detect and manipulate the pose of objects in images, specifically focusing on chairs in this implementation.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Input](#Input)
- [Output](#Output)
- [Description About Steps](#Description-About-Steps)

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

![Input Image](https://github.com/Ayush-chanchal/Object-Segmentation-and-Rotation-Using-Mask-R-CNN/blob/main/images_Of_Chair.jpeg "Input")

## Output

![Output Image](https://github.com/Ayush-chanchal/Object-Segmentation-and-Rotation-Using-Mask-R-CNN/blob/main/image.png "Output")

## Description About Steps

1. Image Loading:

The first step in the process is to load the input image. This image is provided by the user via the command-line interface (CLI).
The image is loaded into the program using OpenCV for further processing.

2. Model Loading:

The Mask R-CNN model is loaded using TensorFlow. This model is pre-trained on the COCO dataset and is capable of detecting and segmenting objects from the image.
The Mask R-CNN model used in this project is mask_rcnn_inception_v2_coco_2018_01_28, which is part of TensorFlow's model zoo.

3. Object Segmentation:

After loading the image, the Mask R-CNN model processes it to detect objects specified by the user (e.g., "chair").
The model creates a mask around the detected object, isolating it from the rest of the image. This mask allows us to work on the object separately from the background.

4. Object Rotation:

Once the object is segmented, the user can specify a rotation angle (azimuth in degrees) to rotate the object.
The segmented object is then rotated around its center by the specified angle using OpenCV functions. The background remains intact during this operation, ensuring that only the object is manipulated.

5. Merging the Object with the Original Background:

After the object is rotated, it is merged back into its original position in the image. The surrounding background remains unchanged.
This step ensures that the rotated object fits seamlessly back into the original scene, maintaining a realistic appearance.

6. Saving the Output:

The final image, with the rotated object and original background, is saved to the specified output path.
The user can specify where the output image should be stored via the command-line argument.


