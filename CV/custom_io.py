import cv2
import numpy as np
import matplotlib.pyplot as plt


def _parse_image_title_pairs(L):
    """Extract (image, title) pairs from flattened list L."""
    pairs = []

    for item in L:
        if type(item) == str:
            pairs[-1][-1] = item
        else:
            pairs.append([item, ''])
    
    return pairs


def plot_images(*args):
    """
    Plot images side-by-side using matplotlib.

    Parameters:
        *args: images and titles

    Example usage:
    >>> plot_images(image1, "title 1", image2, image3, image4, "title 4")
    """
    pairs = _parse_image_title_pairs(args)

    fig, axes = plt.subplots(ncols=len(pairs))
    
    for i, (image, title) in enumerate(pairs):
        ax = axes[i] if len(pairs) > 1 else axes
        ax.axis('off')

        ax.imshow(image, cmap='grey')
        ax.set_title(title)
        
    plt.show()


def plot_images_with_histogram(*args):
    pairs = _parse_image_title_pairs(args)

    fig, axes = plt.subplots(nrows=2, ncols=len(pairs))
    
    for ax in axes.flat:
        ax.axis('off')

    for i, (image, title) in enumerate(pairs):
        col = axes[:, i] if len(pairs) > 1 else axes

        col[0].set_title(title)
        col[0].imshow(image, cmap='grey')

        hist, _ = np.histogram(image, 256, (0, 256))
        cdf = hist.cumsum()
        cdf = cdf / cdf[-1]
        cdf = cdf * max(hist) / max(cdf)
        
        col[1].plot(cdf, 'b--')
        col[1].hist(image.flatten(), 256, [0,256], color='r')
    
    plt.show()


def display_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    