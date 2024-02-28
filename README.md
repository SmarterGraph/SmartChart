# SmartChart
Smartchart is a Python library aimed at automatically generating graphs based on the data source (e.g., CSV file) and user input prompts. It is designed to seamlessly integrate with various Python visualization libraries, such as Matplotlib, Seaborn, Plotly, etc. Additionally, it is intended to be compatible with multiple large language model providers, including OpenAI, open-source LLMs, Hugging Face, etc.

## Code structure

The code is organised as follows

```
|--SmartChart
  |-- smart_chart
    |-- data 
        |-- DataLoader.py
    |-- llms (different types of LLMs)
        |-- open_ai
        |-- other_llms
    |-- plots
        |-- MatplotlibWorker.py
        |-- PlotyWorker.py
        |-- ...
    |-- prompts
        |--base.py
        |--generate_code.py
    |-- tests
    |-- utils
```

## Usage

### Set API Key
Set the open-ai key based on the instructions

[Openai-key-setting](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety/)

### Install the package
```
pip install smart_chart
```

### Run the code
```
python src/SmartChart.py
```
