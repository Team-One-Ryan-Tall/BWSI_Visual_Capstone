import skimage.io as io
def load_image(filepath: str):
    # shape-(Height, Width, Color)
    image = io.imread(str(filepath))
    if image.shape[-1] == 4:
        # Image is RGBA, where A is alpha -> transparency
        # Must make image RGB.
        image = image[..., :-1]  # png -> RGB
    return image
def filenames_from_dict(names_and_numbers: dict, folder="images"):
    out = []
    for name in names_and_numbers.keys():
            for i in range(1, names_and_numbers[name] + 1):
                out.append(f"{folder}/{name}_{i}.jpg")
    return out