import matplotlib
import pandas as pd

matplotlib.use("Agg")
from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import io
import base64
from smart_chart.utils.CodeExecuter import execute_code
from smart_chart.SmartChart import SmartChart
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)
current_filename = "iris_a.csv"  # default value


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    message = request.form["message"]
    # Here, integrate your chatbot logic to get a response.
    # For simplicity, we'll just echo the message back.
    return jsonify({"message": message})


@app.route("/matplotlib", methods=["POST"])
def plot_matplotlib():
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
    return render_template("plot_matplotlib.html", image_data=image_base64)


@app.route("/plotly", methods=["POST"])
def plot_plotly():
    # Get the code from the query parameter
    data = request.json
    code = data["code"]
    df = pd.read_json(data["data"], orient="split")
    fig = go.Figure()

    # Try executing the code
    try:
        fig = execute_code(code, {"go": go, "df": df})
        if fig is None:
            raise ValueError(
                "The provided code did not produce a Plotly figure."
            )
        fig_div = pio.to_html(fig, full_html=False)

    except Exception as e:
        # Handle any errors that arise during code execution
        return f"Error executing the code: {str(e)}", 400
    return render_template("plot_plotly.html", div_placeholder=fig_div)


@app.route("/send_filename", methods=["POST"])
def send_filename():
    global current_filename  # make sure to use the global variable, not a local one
    filename = request.get_json().get("filename")
    print(filename)
    # filename = request.json.get("filename")  # get the file
    if filename and filename.endswith(".csv"):
        current_filename = filename
        return jsonify(success=True), 200
    else:
        return jsonify(success=False, error="Invalid file type"), 400


@app.route("/generate_plot", methods=["POST"])
def generate_plot():
    global current_filename  # refer to the global variable
    message = request.form["message"]
    sc = SmartChart()
    sc.load_data(current_filename)  # use the filename from the global variable
    img1, code1 = sc.plot(
        "matplotlib",
        # "Plot a scatter plot of the sepal length vs sepal width",
        message,
    )
    img2, code2 = sc.plot(
        "plotly",
        # "Plot a scatter plot of the sepal length vs sepal width",
        message,
    )
    return jsonify(
        {"plot1": img1, "code1": code1, "plot2": img2, "code2": code2}
    )


if __name__ == "__main__":
    app.run(debug=True)
