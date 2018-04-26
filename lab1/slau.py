import numpy as np


def slau(x: np.ndarray, y: np.ndarray):
    return np.linalg.inv(x) @ y
