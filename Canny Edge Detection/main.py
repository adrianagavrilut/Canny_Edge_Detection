from sobel_edge_detection import sobelEdgeDetection
from non_max_suppression import non_max_suppression
from threshold_hysteresis import threshold_hysteresis

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def cannyEdgeDetection(
    image: np.ndarray, sigma: int | float, filter_shape, image_format='rgb',
    lowthreshold: float | int = 0.05, highthreshold: float | int = 0.09
):
    G, theta = sobelEdgeDetection(image, sigma, image_format, filter_shape)
    img = non_max_suppression(G, theta)
    img = threshold_hysteresis(img, lowthreshold, highthreshold)
    return img


if __name__ == '__main__':
    path = 'Canny Edge Detection/pngegg.png'
    # path = 'Canny Edge Detection/test.jpg'
    # path = 'Canny Edge Detection/test2.jpg'
    img = np.array(Image.open(path))
    res = cannyEdgeDetection(img, 1.5, (10, 10), 'rgb')
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(res, cmap='gray')
    plt.tight_layout()
    plt.show()
