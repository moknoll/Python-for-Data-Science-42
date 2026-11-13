import pandas as pd

def load(path: str) -> pd.DataFrame | None:
    """Loads a CSV file into a DataFrame.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame | None: DataFrame if successful, None otherwise.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None
