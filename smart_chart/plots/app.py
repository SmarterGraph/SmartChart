import matplotlib
import pandas as pd

matplotlib.use("Agg")
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64
from smart_chart.utils.CodeExecuter import execute_code

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("plot.html")


@app.route("/plot", methods=["POST"])
def plot():
    # Get the code from the query parameter
    data = request.json
    code = data["code"]
    df = pd.read_json(data["data"], orient="split")
    # Pre-defined plotting code, for security
    fig, ax = plt.subplots(figsize=(10, 6))

    # Try executing the code
    try:
        execute_code(code, {"fig": fig, "ax": ax, "df": df})
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getbuffer()).decode("ascii")

    except Exception as e:
        # Handle any errors that arise during code execution
        return f"Error executing the code: {str(e)}", 400
    return render_template("plot.html", image_data=image_base64)


if __name__ == "__main__":
    app.run(debug=True)
