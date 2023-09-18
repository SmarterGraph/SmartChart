from .base import BasePrompt


class GetCode(BasePrompt):
    """
    Prompt for getting python plot package code.
    """

    prompt_context: str = """You are a data scientist. You are asked to analyze a dataset and create a chart
    You are given a dataset 'df' with the following columns: {df_columns}. 
    Your response must include a python code that uses {python_package} library to make a chart of the data using the dataframe 'df'. \
    The chart can be any types of the chart. You can also filter the dataframe as needed. 
    Using the dataframe 'df', return python code with prefix {tag} and suffix {tag} exactly to get the answer to the question: 
    {user_input}
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(tag="```", **kwargs)
