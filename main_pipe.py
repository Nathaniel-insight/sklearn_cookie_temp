# main code to run pipe
# things to do
# - make training pipe
# - make run pipe
# - store processed data
# - store and serialze trained models

from train_pipe import data, clean, preprocess_p, train, evaluate, save_p

def run_main_pipe():
    """
    Runs main pipe
    :return:
    """
    df = data.load_test_data()
    print(df.head())


if __name__ == "__main__":
    run_main_pipe()
