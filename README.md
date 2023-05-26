# Stereo Disparity Map Generator

This code generates a disparity map using the StereoSGBM algorithm. The disparity map represents the difference in pixel coordinates between corresponding points in a pair of stereo images. It provides depth information for each pixel, which can be used for tasks such as 3D reconstruction, object detection, and scene understanding.

## Prerequisites

- Python 2.7 or above
- OpenCV library (version 3.4 or above)
- NumPy library

## Usage

1. Ensure that the required libraries are installed on your system.
2. Place the left and right stereo images in the "images" folder. The left image should be named "im_0.png" and the right image should be named "im_1.png".
3. Modify the algorithm parameters if needed. The parameters are defined in the `parameters` dictionary, and you can adjust them according to your specific requirements.
4. Run the code by executing the following command:
5. The resulting disparity map will be saved as "disparity_map.png" in the same directory as the code.
6. The disparity map, along with the original left and right images, will be displayed on the screen.

## Algorithm Parameters

The following parameters are used for the StereoSGBM algorithm:

- `minDisparity`: The minimum disparity value. Default is 0.
- `numDisparities`: The number of disparity levels. Default is 64.
- `blockSize`: The size of the window used for matching. Default is 8.
- `disp12MaxDiff`: The maximum allowed difference in the left-right disparity check. Default is 1.
- `uniquenessRatio`: The uniqueness ratio used for filtering out false matches. Default is 10.
- `speckleWindowSize`: The maximum allowed size of connected components in the disparity map. Default is 10.
- `speckleRange`: The maximum disparity variation within each connected component. Default is 8.

Feel free to adjust these parameters based on your specific needs.

## Acknowledgments

This code utilizes the OpenCV library, which is an open-source computer vision library. The StereoSGBM algorithm implementation is part of the OpenCV library.

For more information about OpenCV, please visit: [https://opencv.org](https://opencv.org)
