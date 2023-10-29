import webbrowser
import requests
import tempfile
import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
from smart_chart.utils.CodeExecuter import execute_code
import plotly.graph_objs as go
import plotly.io as pio


def generate_plot(url: str, code: str, df: pd.DataFrame) -> None:
    """Generate a plot using the provided code and DataFrame.
    Args:
        url (str): The URL to send the request to.
        code (str): The code to execute.
        df (pd.DataFrame): The DataFrame to use.
    """
    # Send the code and DataFrame to the server
    payload = {
        "code": code,
        "data": df.to_json(orient="split"),
    }
    response = requests.post(
        url,
        json=payload,
    )

    # Check if the server responded with a success status
    if response.status_code != 200:
        print(
            f"Server responded with an error: {response.status_code}. {response.text}"
        )
        return

    # Save the HTML response to a temporary file
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as f:
        url = "file://" + f.name
        f.write(response.text)
    # Open the HTML file in the default web browser
    webbrowser.open(url)


def return_figure(code: str, df: pd.DataFrame, backend: str):
    if backend == "matplotlib":
        # fig, ax = plt.subplots(figsize=(10, 6))
        fig, ax = plt.subplots()
        execute_code(code, {"fig": fig, "ax": ax, "df": df})
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getbuffer()).decode("ascii")
        # return """
        # <div col-md-6>
        # <img src="data:image/png;base64,{}" />
        # </div>
        # """.format(
        #     image_base64
        # )
        return """
            <img src="data:image/png;base64,{}" class="img-fluid"/>
            """.format(
            image_base64
        )
    elif backend == "plotly":
        fig = go.Figure()
        fig = execute_code(code, {"go": go, "df": df})
        fig_div = pio.to_html(fig, full_html=False)
        return fig_div
