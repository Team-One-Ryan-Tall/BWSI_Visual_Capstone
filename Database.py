import pickle
import numpy as np
from CosineDists import cosine_distances
from Profile import Profile

class Database:
    def __init__(self) -> None:
        self.database = {}
    def __repr__(self):
        return str(list(self.database.keys()))
    def __str__(self):
        return str(list(self.database.keys()))
    def add_entry(self, name: str, face_descriptors=None):
        if(name in self.database.keys()):
            self.database[name].add_face_descriptor(face_descriptors)
        self.database[name] = Profile(name, face_descriptors)
    # def remove_entry(self, )
    def saveDatabase(Database:str, FileName: str): 
        with open(FileName, mode = "wb") as opened_file:
            pickle.dump(Database, opened_file)
    def loadDatabase(FileName:str):
        with open(FileName,"rb") as unopened_file:
            Database = pickle.load(unopened_file)
        return Database
    def identify_face(self, face_descriptor: np.ndarray):
        deltas = {}
        for name in self.database:
            dist = cosine_distances(face_descriptor, self.database[name].face_descriptor)
            deltas[dist] = name
        print(deltas)
        return deltas[max(deltas.keys())]