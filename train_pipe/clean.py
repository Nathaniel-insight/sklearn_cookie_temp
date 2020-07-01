from sklearn.base import BaseEstimator, TransformerMixin
from train_pipe import data

class clean_data(BaseEstimator, TransformerMixin):
    # Class Constructor
    def __init__(self):
        return None

    def fit(self):
        return self

    def transform(self, X, y=None):
        X = X.dropna()
        return X


if __name__ == "__main__":
    df = data.load_test_data()
    df_clean = clean_data().transform(df)
    print(df_clean.shape, df.shape)

