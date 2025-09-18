import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Minimal example: choose numeric columns and fill NAs.
    """
    numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    X = df[numeric_cols].copy()
    return X.fillna(0)
