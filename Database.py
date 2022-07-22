import pickle
import numpy as np
from CosineDists import cosine_distances
from Profile import Profile
from Descriptors import descriptors_from_file

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
        minimum = min(deltas.keys())
        if(minimum <= 0.3):
            return deltas[minimum]
        else:
            return "Unknown"
        
    def load_from_dict(self, names_and_numbers: dict):
        names_and_descriptors = {}
        for name in names_and_numbers.keys():
            names_and_descriptors[name] = []
            for i in range(1, names_and_numbers[name] + 1):
                names_and_descriptors[name].append(descriptors_from_file(f"images/{name}_{i}.jpg"))
        for name in names_and_descriptors.keys():
            names_and_descriptors[name] = np.array(names_and_descriptors[name])
            self.add_entry(name, names_and_descriptors[name])
    def get_descriptor(self, name: str):
        return self.database[name].face_descriptor