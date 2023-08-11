import pandas as pd
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[
        patients['condition'].str.startswith('DIAB1') | 
        patients['condition'].str.contains(' DIAB1')
    ]
    return df