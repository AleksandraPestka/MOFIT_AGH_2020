''' 
Calculate the charge density from potential (ex1.py). 
Check the correctness of results.
'''

from itertools import product
import numpy as np
import pandas as pd
from tqdm import tqdm

def calc_rho(phi, delta_x):
    ''' Calculate rho along axis Y '''
    rho = np.zeros((60, 60), dtype='float64')

    for i, j in product(range(1,59), range(1,59)):
        rho[i, j] = (phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1] - \
                    4*phi[i,j])/delta_x**2

    return rho

def calc_results_along_axis(rho, new_rho):
    ground_truth = np.mean(rho, axis=1)
    calculations = np.mean(new_rho, axis=1)
    return ground_truth, calculations        

if __name__ == '__main__':
    delta_x = 1

    # define charge density
    rho = np.zeros((60, 60), dtype='float64')
    rho[20:41, 20:41] = 1.0

    # load Phi calculated in ex1
    phi = pd.read_csv('../data/ex1b.csv', header=0)['Phi'].values.reshape(60, 60)
    
    # calculate rho
    rho_calculated = calc_rho(phi, delta_x)

    # save results
    df = pd.DataFrame(columns=['Y', 'defined', 'calculated'])
    df['Y'] = np.arange(-30,30)
    df['defined'], df['calculated'] = calc_results_along_axis(rho, rho_calculated)
    df.to_csv('../data/ex2.csv', index=False)