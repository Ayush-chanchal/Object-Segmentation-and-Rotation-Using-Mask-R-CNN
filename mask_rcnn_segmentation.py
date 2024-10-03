# mask_rcnn_segmentation.py
import numpy as np
import cv2
import tensorflow as tf

# COCO Labels for object detection
COCO_LABELS = {62: 'chair'}  # Simplified for this example

# Load Mask R-CNN model
def load_model(model_dir):
    try:
        model = tf.saved_model.load(model_dir)
        print("Mask R-CNN model loaded successfully.")
        return model.signatures['serving_default']
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None

# Perform object segmentation using Mask R-CNN
def segment_object(image_path, class_name, azimuth, polar, output_path):
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: The image at path {image_path} could not be loaded.")
        return

    height, width = image.shape[:2]
    print(f"Image loaded successfully: {image_path}")
    print(f"Image dimensions: {height}x{width}")

    # Load the Mask R-CNN model
    detection_model = load_model("mask_rcnn_inception_v2_coco_2018_01_28/saved_model")
    
    if detection_model is None:
        print("Failed to load the Mask R-CNN model.")
        return

    # Prepare image for the model
    input_tensor = tf.convert_to_tensor(np.expand_dims(image, 0), dtype=tf.uint8)

    # Run the detection model
    detections = detection_model(input_tensor)

    # Get detection results
    num_detections = int(detections['num_detections'])
    detection_classes = detections['detection_classes'][0][:num_detections].numpy().astype(np.int64)
    detection_masks = detections['detection_masks'][0][:num_detections]

    print(f"Number of detections: {num_detections}")

    # Find the class in detection results
    for i, detection_class in enumerate(detection_classes):
        if COCO_LABELS.get(detection_class, None) == class_name:
            print(f"Object '{class_name}' found in the image.")
            
            # Create mask
            mask = detection_masks[i].numpy()
            mask = np.where(mask > 0.5, 255, 0).astype(np.uint8)
            mask_resized = cv2.resize(mask, (width, height))

            # Apply red mask to the detected object
            red_mask = np.zeros_like(image)
            red_mask[:, :, 2] = mask_resized  # Set the red channel

            # Isolate the object (masked area)
            object_image = cv2.bitwise_and(image, image, mask=mask_resized)

            # Rotate the object
            rotated_object = rotate_object(object_image, azimuth, polar)

            # Merge rotated object with background
            background = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask_resized))
            final_image = cv2.add(background, rotated_object)

            # Save the output image
            try:
                cv2.imwrite(output_path, final_image)
                print(f"Output image saved at {output_path}")
            except Exception as e:
                print(f"Error saving the image: {e}")
            break
    else:
        print(f"Object '{class_name}' not found in the image.")

# Rotate the object based on azimuth and polar angles
def rotate_object(object_image, azimuth, polar):
    # Rotate the object around the azimuth angle
    center = (object_image.shape[1] // 2, object_image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, azimuth, 1)  # Rotating around azimuth angle
    rotated_image = cv2.warpAffine(object_image, rotation_matrix, (object_image.shape[1], object_image.shape[0]))
    return rotated_image
