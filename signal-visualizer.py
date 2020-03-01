import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

typeOfSignals = ['flicker', 'flicker_harmonics', 'normal',
    'osc_transient', 'swell', 'harmonics', 'interruption_harmonics',
    'sag', 'sag_harmonics', 'swell_harmonics']

for typ in typeOfSignals:
    df = pd.read_csv('dataset/' + typ + '.csv')

    n = np.linspace(0, 10, len(df.iloc[0,:]))

    # for i in range(len(df.iloc[:,0])*):
    plt.figure(typ)
    for i in range(1):    
        plt.scatter(n, df.iloc[i,:])
        plt.title(typ)

plt.show()


