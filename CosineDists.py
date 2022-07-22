import numpy as np

def cosine_distances(X, Y):
    """
    Compute the cosine distance between each row of X and Y.
    """
    if(len(X.shape) > 1):
        X = np.average(X, axis=0)
    if(len(Y.shape) > 1):
        Y = np.average(Y, axis=0)
    
    # print(X.shape)
    # print(Y.shape)
    
    return 1 - (np.dot(X, Y) / (np.linalg.norm(X) * np.linalg.norm(Y)))