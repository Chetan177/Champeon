import numpy as np 
import pandas as pd



def generate_data(data):
    dataframe = pd.DataFrame()
    for i in range(len(data)):
         dataframe["var"+str(i)]= data[i]

    return dataframe
    

    

