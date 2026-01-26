import pandas as pd

# Merge the cleaned metadata with the evaulated move data
def merge_data(meta_df: pd.DataFrame, moves_df: pd.DataFrame) -> pd.DataFrame:
    merged_df = moves_df.merge(meta_df, on='game_id', how='left')
    print(f"Merged {len(meta_df)} games with {len(moves_df)} moves into game dataframe")
    return merged_df