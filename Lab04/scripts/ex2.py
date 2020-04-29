import random

import numpy as np
import pandas as pd
from tqdm import tqdm

from ex1 import metropolis_algorithm

def wave_func(x, y):
    psi = np.pi**(-1/2) * np.exp(-(x**2 + y**2)/2)
    return abs(psi**2)

if __name__ == '__main__':
    pass