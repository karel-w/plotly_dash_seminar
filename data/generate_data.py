import numpy as np
import random
import pandas as pd
import sys

#generate time series analysis data around -1 and 1
def generate_random_array(size):
    array = np.zeros(size)
    center = 1  # Starting center
    
    for i in range(size):
        if random.random() < 0.01:  # Probability of switching centers (adjust as desired)
            center *= -1  # Switch center between -1 and +1
        
        value = np.random.normal(loc=center, scale=0.05)
        array[i] = value

    df = pd.DataFrame(array)
    df.to_csv('time_series.csv')

    return 

if __name__ == '__main__':
    print(f'generating data of size {sys.argv[1]}')
    generate_random_array(int(sys.argv[1]))
    print(f'data generating done')

