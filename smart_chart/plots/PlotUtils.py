import pandas as pd
import webbrowser
import requests
import tempfile


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
