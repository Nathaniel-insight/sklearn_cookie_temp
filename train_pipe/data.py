from sklearn.datasets import load_iris


def load_test_data():
    """
    load iris data for testing purposes
    """
    df = load_iris(return_X_y=True)

    return df

