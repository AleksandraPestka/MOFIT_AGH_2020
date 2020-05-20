import sys

from itertools import product
import numpy as np
import pandas as pd
from tqdm import tqdm
import math

np.set_printoptions(threshold=sys.maxsize)

if __name__ == '__main__':
    # define steps
    delta_x = 1
    delta_y = 1
    delta_omega = 0.01

    # define charge density
    rho = np.zeros((60, 60), dtype='float64')
    rho[20:41, 20:41] = 1.0

    # define dataset to save results 
    df = pd.DataFrame(columns=['omega', 'iterations'])

    for omega in tqdm(np.arange(1, 2, step=delta_omega)):
        # initially define zero potential 
        phi = np.zeros((60, 60), dtype='float64')

        total_integral = 0
        iteration = 0 

        while(True):
            iteration += 1
            tmp_integral = 0

            # iterate over points excluding edges (where phi = 0)
            # use product function instead of nested for loops
            for i, j in product(range(1,59), range(1,59)):
                # calculate new value for potential
                phi[i, j] = (1.0-omega) * phi[i, j] + omega * \
                            (phi[i+1, j] + phi[i-1, j] + \
                            phi[i, j+1] + phi[i, j-1] + rho[i,j] * \
                            delta_x**2)/4.0         

            # calculate integral
            for i,j in product(range(1,59), range(1,59)):
                tmp_integral += 0.5 * \
                                ((((phi[i+1, j] - phi[i-1, j])/(2*delta_x)))**2 + \
                                ((phi[i, j+1] - phi[i, j-1])/(2*delta_y))**2) - \
                                rho[i, j] * phi[i, j]
            
            if (abs(tmp_integral - total_integral) < 1):
                break

            total_integral = tmp_integral

        df.loc[len(df)] = (omega, iteration)
        print(omega, iteration)

    # save dataframe to file
    df.to_csv('../data/ex1.csv', index=False)
