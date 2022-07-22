

import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
from facenet_models import FacenetModel
from matplotlib.patches import Rectangle
from LoadImage import load_image

def detect(model: FacenetModel,filepath: str):
    return model.detect(load_image(filepath))

def detect_arr(model: FacenetModel,img: np.ndarray):
    return model.detect(img)

def display_boxes(model: FacenetModel, filepath: str):
    fig, ax = plt.subplots()
    img = load_image(filepath)
    ax.imshow(img)
    boxes, probabilities, landmarks = model.detect(img)

    for box, prob, landmark in zip(boxes, probabilities, landmarks):
        ax.add_patch(Rectangle(box[:2], *(box[2:] - box[:2]), fill=None, lw=2, color="red"))

def display_boxes_arr(model: FacenetModel, img: np.ndarray):
    fig, ax = plt.subplots()
    ax.imshow(img)
    boxes, probabilities, landmarks = model.detect(img)

    for box, prob, landmark in zip(boxes, probabilities, landmarks):
        ax.add_patch(Rectangle(box[:2], *(box[2:] - box[:2]), fill=None, lw=2, color="red"))
        
def boxes_and_image(model: FacenetModel, filepath: str):
    img = load_image(filepath)
    return model.detect(img), img