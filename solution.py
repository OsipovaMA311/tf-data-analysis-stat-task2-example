import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    alpha1 = (1 - p)/2
    alpha2 = (1+p)/2
    n = x.size
    alpha1, alpha2 = pow(alpha1, 1/n), pow(alpha2, 1/n)
    
    x_max = x.max()
    return (x_max - 0.059)/alpha2 + 0.059, \
           (x_max - 0.059)/alpha1 + 0.059
