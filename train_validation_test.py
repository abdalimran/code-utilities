from typing import Tuple
import pandas as pd
import numpy as np


def train_validation_test(data: pd.DataFrame, train_pct: float, validation_pct: float, stratification_col: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Function that takes a pandas dataframe and returns stratified samples
        of train, validation, and test sets using the given percentage, and
        stratification column. Sum of train_pct & validation_pct must be <= 1.0.

    Args:
        data (pd.DataFrame): Dataset
        train_pct (float): Percentage of training data (<1.0)
        validation_pct (float): Percentage of validation data (<1.0)
        stratification_col (str): Column for stratified sampling

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
            Train, Validation, and Test dataset in pandas DataFrame.
    """
    test_pct = 1.0 - (train_pct + validation_pct)

    training_data = (data
                     .groupby(stratification_col, group_keys=False)
                     .apply(lambda x: x.sample(frac=train_pct,
                                               random_state=2023))
                     )

    rest_data = data[~data.index.isin(training_data.index)]

    validation_pct = validation_pct / (validation_pct + test_pct)
    test_pct = test_pct / (validation_pct + test_pct)

    validation_data = (rest_data
                       .groupby(stratification_col, group_keys=False)
                       .apply(lambda x: x.sample(frac=validation_pct,
                                                 random_state=2023))
                       )

    test_data = rest_data[~rest_data.index.isin(validation_data.index)]

    return training_data, validation_data, test_data


if __name__ == "__main__":
    data = pd.read_csv("data.csv")
    training_data, validation_data, test_data = train_validation_test(
        data, 0.80, 0.15, 'labels')
