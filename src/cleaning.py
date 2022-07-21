import pandas as pd
import numpy as np
import seaborn as sns


def fatality_clean(string):
"""
This function Cleans the fatality Column and returns it in an readable format

It takes a String If the string is y or n or other meaning for yes and no it will returns a Dead for yes on fatal and returns Survived of Not

"""
    
    string = str(string).lower().strip()
    if "yes" in string or "y" in string or "s" in string:
        return "Dead"
    elif "no" in string or "Neg" in string or "n" in string:
        return "Survived"
    else:
        return np.nan
    
def drop_na(df,cat):
    """"
    This function takes a DataFrame and drops all missing values in the given column name
    
    """"
    return df.dropna(subset=[cat],inplace=True)

def stripp(x):
    """
    This Function is a normal .strip function but for the iteration of a column  
    """
    return x.strip()






