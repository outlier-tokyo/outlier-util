"""
モデリング前のデータセット整理に関する便利機能
"""
import pandas as pd
from sklearn.model_selection import KFold

def get_kfold(data : pd.DataFrame, param_kf : dict):
    """
    <概要>
    Parameters
    ----------
    data : pd.DataFrame
        対象データ
    param_kf : dict
        KFoldのパラメータ
    Returns
    ----------
    kfold : 2d-array

    Examples
    --------
    get_kfold(data=df, param_kf={"n_splits": 5, "shuffle" : True, "random_state" : 42})
    """
    print("hello")
    kf = KFold(**param_kf)
    return [
        [data.iloc[train_index], data.iloc[test_index]]
        for train_index, test_index in kf.split(data)
    ]

def _template():
    """
    <概要>
    Parameters
    ----------
    <param_name> : <format>, <default>
        <describe>
    Returns
    ----------
    <name> : <format>, <default>
        <describe>
    See Also
    --------
    <xxx>
    Notes
    -----
    <xxx>
    Examples
    --------
    <xxx>
    """
    print("hello world")
