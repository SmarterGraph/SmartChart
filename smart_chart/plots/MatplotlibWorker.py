import pandas as pd
from smart_chart.plots.PlotUtils import generate_plot


def matplotlib_run_code(code: str, df: pd.DataFrame) -> None:
    """Generate a Matplotlib plot using the provided code and DataFrame.

    Args:
        code (str): The code to execute.
        df (pd.DataFrame): The DataFrame to use.
    """
    url = "http://127.0.0.1:5000/matplotlib"
    generate_plot(url, code, df)


if __name__ == "__main__":
    df = pd.read_csv("iris.csv", index_col=False)
    code = """x = df["sepal.length"].tolist(); y = df["sepal.width"].tolist() ; ax.plot(x, y); ax.set_title('Generated Plot')"""
    matplotlib_run_code(code, df)
