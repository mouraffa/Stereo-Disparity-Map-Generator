import numpy as np
import cv2

def main():
    """
        Main function to compute the disparity map using the StereoSGBM algorithm.
    """
    # Load and resize left image
    imgL = cv2.imread("images/im0.png", 0)
    imgL = cv2.resize(imgL, (600, 600))

    # Load and resize right image
    imgR = cv2.imread("images/im1.png", 0)
    imgR = cv2.resize(imgR, (600, 600))

    # Set parameters for StereoSGBM algorithm
    parameters = {
        'minDisparity': 0,
        'numDisparities': 64,
        'blockSize': 8,
        'disp12MaxDiff': 1,
        'uniquenessRatio': 10,
        'speckleWindowSize': 10,
        'speckleRange': 8
    }

    # Create StereoSGBM algorithm object with specified parameters
    stereo = cv2.StereoSGBM_create(**parameters)

    # Compute disparity using the StereoSGBM algorithm
    disp = stereo.compute(imgL, imgR).astype(np.float32)

    # Normalize the disparity map
    disp = cv2.normalize(disp, 0, 255, cv2.NORM_MINMAX)

    # Save the disparity map
    cv2.imwrite("disparity_map.png", disp)

    # Display the disparity map and original images
    cv2.imshow("Disparity", disp)
    cv2.imshow("Left Image", imgL)
    cv2.imshow("Right Image", imgR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
