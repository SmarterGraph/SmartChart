import matplotlib.pyplot as plt
import pandas as pd
import webbrowser
import requests
import tempfile


def matplotlib_run_code(code: str, df: pd.DataFrame) -> None:
    url = "http://127.0.0.1:5000/plot"

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


if __name__ == "__main__":
    df = pd.read_csv("iris.csv", index_col=False)
    code = """x = df["sepal.length"].tolist(); y = df["sepal.width"].tolist() ; ax.plot(x, y); ax.set_title('Generated Plot')"""
    matplotlib_run_code(code, df)
