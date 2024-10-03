# cli.py
import argparse
from mask_rcnn_segmentation import segment_object

def main():
    parser = argparse.ArgumentParser(description="Segment and rotate an object using Mask R-CNN")
    parser.add_argument('--image', required=True, help="Path to the input image")
    parser.add_argument('--class_name', required=True, help="Class of the object (e.g., 'chair')")
    parser.add_argument('--azimuth', type=float, required=True, help="Rotation angle in degrees")
    parser.add_argument('--output', required=True, help="Path to save the output image")

    args = parser.parse_args()

    print(f"Running segmentation on image: {args.image}")
    print(f"Class name: {args.class_name}")
    print(f"Rotation angle (azimuth): {args.azimuth}")
    print(f"Output will be saved to: {args.output}")

    # Call the object segmentation and rotation function
    segment_object(args.image, args.class_name, args.azimuth, 0, args.output)

    print("Segmentation and rotation completed.")

if __name__ == "__main__":
    main()
