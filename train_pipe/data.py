from sklearn.datasets import load_iris
import pandas as pd

def load_test_data():
    """
    load iris data for testing purposes
    """
    df_x, df_y = load_iris(return_X_y=True, as_frame=True)

    df = pd.concat([df_x, df_y])

    return df
