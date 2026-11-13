import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def create_plot(df: pd.DataFrame, country: str) -> None:
    """ This Function takes a Dataframe and a string country
        And creates a lot which shows life expectancy for the given
        year

    Args:
        df (pd.DataFrame): _description_
        country (str): _description_
    """

    df = df[df["country"] == country]
    x = df.columns[1:].astype(int)
    y = df.iloc[0, 1:]

    # plt.plot(x, y), df.columns[1] because 0 is country
    # df.iloc[0], will give us access to index location at 0, 1:end
    plt.plot(x, y)

    plt.xlabel("Years")
    plt.ylabel("life expectancy")
    plt.title(f"life expectancy in {country}")
    plt.show()


def main():
    df = load("./life_expectancy_years.csv")
    create_plot(df, "France")


if __name__ == "__main__":
    main()
