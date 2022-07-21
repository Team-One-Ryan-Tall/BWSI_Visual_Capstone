%matplotlib notebook
import matplotlib.pyplot as plt
# from camera import take_picture
import numpy as np
from facenet_models import FacenetModel
from matplotlib.patches import Rectangle



model = FacenetModel()

boxes, probabilities, landmarks = model.detect(# insert some image)

    
fig, ax = plt.subplots()
ax.imshow(pic)

for box, prob, landmark in zip(boxes, probabilities, landmarks):
    # draw the box on the screen
    ax.add_patch(Rectangle(box[:2], *(box[2:] - box[:2]), fill=None, lw=2, color="red"))