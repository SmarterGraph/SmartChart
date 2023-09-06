import plotly.graph_objects as go
from utils.CodeExecuter import CodeExecuter
import pandas as pd


def plotly_run_code(code: str, df: pd.DataFrame) -> None:
    """Run the plotly code generated by the API.
    Args:
        code (str): The code to run.
        df (pd.DataFrame): The DataFrame to use.
    """
    imports = {"go": go, "df": df}
    CodeExecuter.execute_code(code, imports)