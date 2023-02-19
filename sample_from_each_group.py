import pandas as pd
from typing import Union, Optional


def sample_from_each_group(data: pd.DataFrame,
                           group_col: str,
                           n: Union[int, None],
                           frac: Optional[Union[float, None]] = None) \
                           -> pd.DataFrame:
    """Function that takes a pandas dataframe and returns a sample from each
        group given by the number of samples or percentage.

    Args:
        data (pd.DataFrame): Dataset
        group_col (str): Column name of the group
        n (Union[int, None]): Number of samples want from each group
        frac (Optional[Union[float, None]]): % of samples want from each group
            Defaults to None

    Returns:
        pd.DataFrame: Sampled data
    """
    sample = (data
              .groupby(group_col, group_keys=False)
              .apply(lambda x: x.sample(n=n, frac=frac, random_state=2023))
              )
    
    return sample
