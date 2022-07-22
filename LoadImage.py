import skimage.io as io
def load_image(filepath: str):
    # shape-(Height, Width, Color)
    image = io.imread(str(filepath))
    if image.shape[-1] == 4:
        # Image is RGBA, where A is alpha -> transparency
        # Must make image RGB.
        image = image[..., :-1]  # png -> RGB
    return image