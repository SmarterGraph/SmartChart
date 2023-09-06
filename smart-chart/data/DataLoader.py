import pandas as pd
import os


def load_file_into_dataframe(filename) -> pd.DataFrame:
    """Load a file into a Pandas DataFrame based on its extension.
    Args:
        filename (str): The name of the file to load.
    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not exist!")

    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension == ".csv":
        return pd.read_csv(filename, index_col=False)
    elif file_extension == ".json":
        return pd.read_json(filename)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")
