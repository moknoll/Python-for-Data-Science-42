import pandas as pd


def load(path: str) -> pd.DataFrame:
    """This Function takes csv file and loads it to a Dataframe

    Args:
        path (str): csv File

    Returns:
        pd.DataFrame
    """
    df = pd.read_csv(path)
    # print(f"Loading dataset of dimensions {df.shape}")
    return df
