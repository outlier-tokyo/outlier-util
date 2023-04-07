"""
sklearnに存在しない回帰用の評価指標
"""
import numpy as np
import pandas as pd

def mape(y_true, y_pred, agg=True):
    """
    <概要>
    Parameters
    ----------
    Returns
    ----------
    Examples
    --------
    mape(y_true=actual, y_pred=predict)
    """
    diff = y_pred - y_true
    diff_pct = diff / abs(y_true)
    if not agg: return diff_pct
    return np.mean(abs(diff_pct))

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
    print("hello")