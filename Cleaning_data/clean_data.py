# Libraries
import pandas as pd
import numpy as np

def clean_data(file_name):
    '''
    This function will clean the data and remove any unnecessary
    columns or columns that don't hold useful information
    
    Input: string with .csv file extension
    Output: Clean data frame
    '''
    assert isinstance(file_name,str), "file_name is not a string"
    # Read the file
    df = pd.read_csv(file_name, encoding='utf-8')
    # Make the column names upper_case
    df.columns = df.columns.str.upper()
    # Dropping Columns that are not needed
    try:
        df.drop(["ID", "NAME", "HOST_NAME", "HOST_ID", "NEIGHBOURHOOD_GROUP"], axis=1, inplace=True)
    except:
        df.drop(["ID", "NAME", "HOST_NAME", "HOST_ID"], axis=1, inplace=True)        
    df.drop(["LAST_REVIEW", "REVIEWS_PER_MONTH"], axis=1, inplace=True)
    df.columns = df.columns.str.lower()
    return df