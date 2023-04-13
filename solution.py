import pandas as pd
import numpy as np


chat_id = 332487463 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    eps = 0.07
    F = lambda x: binom.cdf(k = x, n = y_cnt, p = x_success / x_cnt)
    p = 1 - F(y_success)
    return False if p > eps else True
