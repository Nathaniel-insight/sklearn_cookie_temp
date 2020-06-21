# main code to run pipe
# things to do
# - make training pipe
# - make run pipe
# - store processed data
# - store and serialze trained models

from train_pipe import data, clean, preprocess_p, train, evaluate, save_p

df = data.load_test_data()

print(df.head())2