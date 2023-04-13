import pandas as pd
import numpy as np


chat_id = 332487463 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    eps = 0.07
    
    return False if x_success / x_cnt <= y_success / y_cnt - eps else True
