import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

def proba_func(x):
    return np.pi**(-1/2)*np.exp(-x**2)

def execute_one_step(x):
    delta_t = random.uniform(-1/4, 1/4) # random shift
    x_proposed = x + delta_t            # temporary x position
    y = random.uniform(0, 1)            # just random number from range [0,1]

    if y < (proba_func(x_proposed) / proba_func(x)):
        x_next = x_proposed
    else: 
        x_next = x

    return x_next

def calc_moment(x_vec, order):
    moment_value = 0

    for var in x_vec:
        moment_value += (var**order * proba_func(var))

    return moment_value

def avg_moment(x_vec, order):
    return sum(np.power(x_vec, order))/len(x_vec)

if __name__ == '__main__':
    x = 0          # initial position
    df = pd.DataFrame(columns=['l', 'I1', 'I2', 'I3', 'I4'])

    # l : number of steps
    #for l in range(1, int(1e7)):
    for l in [1000000]:
        x_list = []
        for step in range(l):
            x = execute_one_step(x)
            x_list.append(x)

        # calculate 1st, 2nd, 3rd, 4th moment 
        for n in [1,2,3,4]:
            print(avg_moment(x_list, n))
            print()

        # the distribution of x must be similar to proba_func
        sns.distplot(x_list, hist=True, kde=True, label='random walk')
        plt.show()
            
            