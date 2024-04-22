import numpy as np

def mse(y: np.ndarray) -> float:
    """Calculate the MSE of a vector"""
    mse = np.mean((y - np.mean(y)) ** 2)
    return mse

def weighted_mse(y_left: np.ndarray, y_right: np.ndarray) -> float:
    """Calculate the weighted MSE of two vectors."""
    
    mse_left = mse(y_left)
    mse_right = mse(y_right)

    N_left = y_left.size
    N_right = y_right.size

    mse_weighted = ((mse_left * N_left) + (mse_right * N_right)) / (N_left + N_right)

    return mse_weighted
