import pandas as pd

# Remove unecessary columns from metadata dataframe
def remove_unnec(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Columns for removal
    cols = ['Event','Site','Round','CurrentPosition','Timezone','Date','UTCTime','Link']

    # Drop columns and return dataframe
    df.drop(columns=cols, inplace=True, errors='ignore')
    return df