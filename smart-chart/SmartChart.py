import pandas as pd
from llms.openai import OpenAI
from prompts.get_matplotlib_code import GetMatplotlibCode
from data.DataLoader import load_file_into_dataframe
from plots.MatplotlibWorker import matplotlib_run_code
from plots.PlotlyWorker import plotly_run_code
from typing import Optional


class SmartChart:
    """Smart Chart class that uses the OpenAI API to generate code."""

    def __init__(self, api_key: Optional[str] = None, **kwargs) -> None:
        self.llm = OpenAI(api_key=api_key, **kwargs)

    def load_data(self, filename: str) -> None:
        """Load a file into a Pandas DataFrame based on its extension.
        Args:
            filename (str): The name of the file to load.
        """
        self.df = load_file_into_dataframe(filename)
        self.columns = self.df.columns.tolist()

    def plot(self, backend: str, question: str) -> None:
        """Plot a chart based on the question.
        Args:
            backend (str): The backend to use. Either "matplotlib" or "plotly".
            question (str): The question to answer.
        """
        self.inputs = {
            "question": question,
            "columns": self.columns,
        }
        instructions = str(GetMatplotlibCode(**self.inputs))

        code = self.llm.generate_code(instructions)

        if backend == "matplotlib":
            matplotlib_run_code(code, self.df)
        elif backend == "plotly":
            plotly_run_code(code, self.df)
        else:
            raise ValueError(f"Unsupported backend: {backend}")


if __name__ == "__main__":
    sc = SmartChart()
    sc.load_data("data/iris.csv")
    sc.plot(
        "matplotlib", "Plot a scatter plot of the sepal length vs sepal width"
    )
