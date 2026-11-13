from load_csv import load
import pandas as pd
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


def project_life(df1: pd.DataFrame, df2: pd.DataFrame) -> None:
    """ This Function Takes two dataFrames and cleans the data.
        It Shows a scatterplot between these two points.
    Args:
        df1 (pd.DataFrame):
        df2 (pd.DataFrame): _description_
    """

    gdp = df1[["1900", "country"]]
    life_exc = df2[["1900", "country"]]

    merged = pd.merge(gdp, life_exc, on="country")
    merged = merged.drop(columns='country')
    merged = merged.rename(columns={"1900_x": "GDP", "1900_y": "Life Expectancy"})

    columns = ["GDP", "Life Expectancy"]
    merged[columns] = merged[columns].apply(lambda col: col.map(clean))

    merged.plot.scatter(x='Life Expectancy', y='GDP', )
    plt.xlabel("GDP")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.show()

    return


def main():
    """T    """
    try:
        path1 = "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        path2 = "./life_expectancy_years.csv"
        df1 = load(path1)
        df2 = load(path2)
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        project_life(df1, df2)


if __name__ == "__main__":
    main()
