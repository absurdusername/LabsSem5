import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_images(*args, ncols=-1):
    """
    Plot images side-by-side using matplotlib.

    Parameters:
        *args: list of image and titles
        ncols (int): maximum number of images in each row of the plot

    Example usage:
    >>> plot_images(image1, "title 1", image2, image3, image4, "title 4")
    """
    pairs = []

    for a in args:
        if type(a) == str:
            pairs[-1][-1] = a
        else:
            pairs.append([a, ''])

    fig, axes = plt.subplots(ncols=len(pairs))
    
    for i, (image, title) in enumerate(pairs):
        ax = axes[i] if len(pairs) > 1 else axes
        ax.imshow(image, cmap='grey')
        ax.set_title(title)
        ax.axis('off')
    
    plt.show()


def display_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)