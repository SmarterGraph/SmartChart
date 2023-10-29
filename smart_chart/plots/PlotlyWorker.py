import pandas as pd
from smart_chart.plots.PlotUtils import generate_plot, return_figure


def plotly_run_code(code: str, df: pd.DataFrame) -> None:
    """Generate a Plotly plot using the provided code and DataFrame.
    Args:
        code (str): The code to execute.
        df (pd.DataFrame): The DataFrame to use.
    """
    url = "http://127.0.0.1:5000/plotly"
    if "fig.show()" in code:
        code = code.replace("fig.show()", "")
    generate_plot(url, code, df)


def plotly_return_figure(code: str, df: pd.DataFrame) -> str:
    """Generate a Matplotlib plot using the provided code and DataFrame.

    Args:
        code (str): The code to execute.
        df (pd.DataFrame): The DataFrame to use.
    """
    if "fig.show()" in code:
        code = code.replace("fig.show()", "")
    return return_figure(code, df, "plotly")


if __name__ == "__main__":
    df = pd.read_csv("iris.csv", index_col=False)
    code = """x = df["sepal.length"].tolist(); y = df["sepal.width"].tolist() ; fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')], layout=go.Layout(title="Simple Plot from Flask"))"""
    plotly_run_code(code, df)
