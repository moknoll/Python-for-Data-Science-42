import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt


def clean(value: str) -> float:
    """ This Functions Takes a string number witk k or M
        and returns the number as a float.

    Args:
        value (str): Number as string

    Returns:
        float: Calculated number
    """
    if pd.isna(value):
        return value

    if isinstance(value, (int, float)):
        return float(value)

    if value.endswith("k"):
        return float(value[:-1]) * 1000

    elif value.endswith("M"):
        return float(value[:-1]) * 1000000

    else:
        return float(value)


def create_plot(df: pd.DataFrame, country1: str, country2: str) -> None:

    df = df[(df["country"] == country1) | (df["country"] == country2)].copy()
    # print(df)
    # df = df.iloc[0:1, 1:-50]
    years = df.columns[1:]
    # print(years)

    # Apply the clean() function to every value in the year columns.
    # apply() iterates over the columns, while map() processes each individual value.
    # The cleaned values are then stored back in the DataFrame.
    df[years] = df[years].apply(lambda col: col.map(clean))
    # Transpose the DataFrame
    df = df.set_index("country").T
    df.index = df.index.astype(int)

    # Convert all values to numeric data types
    df = df.astype(float)

    df.plot(figsize=(12, 5))

    plt.xticks(range(1800, 2050, 40))
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(f"Population: {country1} vs {country2}")
    plt.grid()
    plt.tight_layout()
    plt.show()


def main():
    try:
        df = load("./population_total.csv")
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        create_plot(df, "France", "Germany")


if __name__ == "__main__":
    main()
