import numpy as np

class Profile:
    def __init__ (self, name: str,  face_descriptors=None):
        if(face_descriptors is not None):        
            self.count = len(face_descriptors)
            if(len(face_descriptors.shape) == 1):
                face_descriptors = np.array([face_descriptors])
            elif (len(face_descriptors.shape) == 2):
                face_descriptors = np.average(face_descriptors, axis=0)
        else:
            self.count = 0
        self.face_descriptor = face_descriptors
        self.name = name
    @property
    def properties(self):
        return (self.name, self.face_descriptor)
    def __repr__(self):
        return self.name
    def add_face_descriptor(self, face_descriptor):
        if(face_descriptor is not None):
            assert isinstance(face_descriptor, np.ndarray)
            assert face_descriptor.shape == (512,)
            if(self.face_descriptor is None):
                self.face_descriptor = face_descriptor
                self.count = 1
            elif(len(face_descriptor) == 0):
                self.face_descriptor = face_descriptor
                self.count = 1
            else:
                (self.face_descriptor * self.count + face_descriptor)/(self.count + 1)
                self.count += 1