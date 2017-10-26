import numpy as np


def deviance(arr: np.array) -> float:
    if np.sum(arr) == 0:
        return 1e10
    return np.std(arr)
