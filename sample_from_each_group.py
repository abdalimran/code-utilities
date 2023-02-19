import pandas as pd
from typing import Union


def sample_from_each_group(data: pd.DataFrame,
                           n: Union[int, None],
                           frac: Union[float, None],
                           group_col: str) -> pd.DataFrame:
    """Function that takes a pandas dataframe and returns a sample from each
        group given by the number of samples or percentage.

    Args:
        data (pd.DataFrame): Dataset
        n (Union[int, None]): Number of samples want from each group
        frac (Union[float, None]): % of samples want from each group
        group_col (str): Column name of the group

    Returns:
        pd.DataFrame: Sampled data
    """
    sample = (data
              .groupby(group_col, group_keys=False)
              .apply(lambda x: x.sample(n=n, frac=frac, random_state=2023))
              )
    
    return sample
