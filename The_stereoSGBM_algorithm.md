# StereoSGBM Algorithm

The StereoSGBM algorithm involves several mathematical concepts and computations. This section explains the key steps and the math behind them.

## Cost Computation

For each pixel in the left image (L(x, y)) and its corresponding pixel in the right image (R(x - d, y)) with a specific disparity value (d), the cost (C(d)) can be computed using the sum of squared differences (SSD) or absolute differences (SAD) between the pixel intensities.

The cost computation can be represented as follows:
- SSD: C(d) = ∑ (L(x, y) - R(x - d, y))^2
- SAD: C(d) = ∑ |L(x, y) - R(x - d, y)|

Here, the summation is performed over a defined neighborhood around the pixel.

## Cost Aggregation

Cost aggregation is performed to obtain a smoother disparity map and handle noise and ambiguity. One approach is to compute a cost volume (V(d, x, y)) representing the aggregated matching costs for each disparity value at every pixel location (x, y). This is achieved by aggregating costs over a local neighborhood using techniques like block matching or adaptive support weight aggregation.

## Disparity Optimization

To find the disparity values that minimize the total matching cost and ensure global consistency, a dynamic programming technique called semi-global matching (SGM) is often used. SGM involves computing costs along multiple directions (horizontally, vertically, and diagonally) and accumulating the costs to find the disparity values that minimize the total cost.

## Disparity Refinement

Disparity refinement is a common technique used to estimate disparity values with higher precision. Sub-pixel interpolation is one such refinement method. It involves fitting a curve to the matching costs around the minimum cost disparity value and finding the minimum point of the curve, which corresponds to a sub-pixel disparity value.

Now, let's consider a simple example to illustrate the StereoSGBM algorithm:

Assuming we have two grayscale stereo images, left_image and right_image, of size MxN pixels, the algorithm progresses as follows:

1. Cost Computation:
   For each pixel (x, y) in the left_image, we compute the matching cost by comparing its intensity value with the corresponding pixels in the right_image for different disparity values.

2. Cost Aggregation:
   We aggregate the computed costs over a local neighborhood for each pixel, resulting in a cost volume V(d, x, y) of size DxMxN, where D is the number of disparity levels.

3. Disparity Optimization:
   We apply the semi-global matching (SGM) algorithm to the cost volume to find the disparity values that minimize the total cost. This involves computing costs along multiple directions and accumulating the costs to determine the optimal disparities.

4. Disparity Refinement:
   Sub-pixel interpolation can be performed on the resulting disparity map to estimate sub-pixel disparities, providing more precise depth information.

By following these steps, the StereoSGBM algorithm generates a disparity map that represents the difference in pixel coordinates between corresponding points in the stereo images, providing depth information for the scene.

