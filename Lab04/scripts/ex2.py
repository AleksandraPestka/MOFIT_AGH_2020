import random

import numpy as np
import pandas as pd
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

def wave_func(x, y):
    psi = np.pi**(-1/2) * np.exp(-(x**2 + y**2)/2)
    return abs(psi**2)

def metropolis_algorithm_2D(x, y, dist_func):
    delta_t_x = random.uniform(-1/4, 1/4)     
    delta_t_y = random.uniform(-1/4, 1/4)
    x_proposed = x + delta_t_x             
    y_proposed = y + delta_t_y 
        
    z = random.uniform(0, 1)                

    if z < (dist_func(x_proposed, y_proposed) / dist_func(x, y)):
        return x_proposed, y_proposed
   
    return x,y

def calc_energy(x_vec, y_vec, steps):
    return (1/steps) * sum(np.add(np.square(x_vec), np.square(y_vec)))/2

if __name__ == '__main__':
    MODE = 'energy'
    # initial conditions
    x, y = 0, 0
    
    if MODE == 'walk':
        # first part
        l = 100000
        
        x_list, y_list = [], []

        for step in range(l):
            x, y = metropolis_algorithm_2D(x, y, wave_func)
            x_list.append(x)
            y_list.append(y)

        df = pd.DataFrame({'x': x_list, 'y': y_list})
        df.to_csv('../data/ex2.csv')

    elif MODE == 'energy':
        # second part
        df = pd.DataFrame(columns=['l', 'E'])

        # l : number of steps
        for l in tqdm(np.logspace(start=1, 
                                stop=7, 
                                endpoint=True,
                                num=100,
                                dtype='int32')):
            df_row = []
            df_row.append(l)
            
            x_list = []
            y_list = []
            for step in range(l):
                x, y = metropolis_algorithm_2D(x, y, wave_func)
                x_list.append(x)
                y_list.append(y)

            # calculate potential energy
            df_row.append(calc_energy(x_list, y_list, l))
            df.loc[len(df)] = df_row

        df.to_csv('../data/ex2_energy.csv', index=False)
