import pandas as pd
from llms.gpt_all import OpenAI
from prompts.generate_code import GetCode
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
        instructions = str(
            GetCode(
                df_columns=self.columns,
                user_input=question,
                python_package=backend,
            )
        )
        code = self.llm.query_chat_completion(instructions).split("```")[1]
        print(code)
        # code = self.llm.generate_code(instructions)

        if backend == "matplotlib":
            matplotlib_run_code(code, self.df)
        elif backend == "plotly":
            plotly_run_code(code, self.df)
        else:
            raise ValueError(f"Unsupported backend: {backend}")


if __name__ == "__main__":
    sc = SmartChart()
    sc.load_data("iris.csv")
    sc.plot("plotly", "Plot a scatter plot of the sepal length vs sepal width")
