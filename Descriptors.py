
from facenet_models import FacenetModel

from BoundedBox import boxes_and_image


model = FacenetModel()

def descriptors_from_file(filepath: str):
    #boxes, probabilities, landmarks
    bpl, image = boxes_and_image(model, filepath)
    boxes, probabilities, landmarks = bpl
    return model.compute_descriptors(image, boxes)

def descriptors_from_filestack(filepaths: list):
    descriptor_stack = []
    for filepath in filepaths:
        descriptor_stack.append(descriptors_from_file(filepath))
    return descriptor_stack