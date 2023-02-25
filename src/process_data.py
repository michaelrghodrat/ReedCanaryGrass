""" 
=== Module Description ===
A module to contain code relating to the extraction phase of iNaturalist Data
"""

import pandas as pd

PATH_TO_RCG_DATA = "C:/Users/micha/Documents/ReedCanaryGrass/Data/rcg_02_04_23.csv"
PATH_TO_GBR_DATA = "C:/Users/micha\Documents/ReedCanaryGrass/Data/gbr_01_28_23.csv"
PATH_TO_BR_DATA = "C:/Users/micha/Documents/ReedCanaryGrass/Data/Bulrush_01_28_23.csv"


def extract_data() -> pd.DataFrame:
    """Extracts iNaturalist data from csv and saves result in a pandas DataFrame
    """
    rcg_df =  pd.read_csv(PATH_TO_RCG_DATA, sep='\t')
    br_df = pd.read_csv(PATH_TO_BR_DATA, sep='\t')
    gbr_df = pd.read_csv(PATH_TO_GBR_DATA, sep='\t')

    df = pd.concat([rcg_df, br_df, gbr_df])

    return df




    

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove records that are missing key attributes like year, location, etc.
    """
    original_size = df.shape[0]
    df.dropna(axis=0, subset = ['gbifID', 'scientificName', 'year', 'basisOfRecord', 'species', 'decimalLatitude', 'decimalLongitude'], inplace=True)
    #print(f"dropped {original_size - df.shape[0]} records after removing null records")
    
    df.drop(df.loc[df['year'] >= 2023].index, inplace=True)
    df = df.astype({
        'year': int
    })
    print(f"dropped {original_size - df.shape[0]} records after removing null records")
    print(df.dtypes)

    return df



def extract_and_clean() -> pd.DataFrame:
    """Extracts and cleans iNaturalist data from csv and returns result 
    in a pandas DataFrame
    """
    return clean_data(extract_data())

    


    









if __name__ == '__main__':
    #print(extract_data())
    print(clean_data(extract_data()))


