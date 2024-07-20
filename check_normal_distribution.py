import numpy as np
from scipy import stats

def check_normal_distribution(data):
    
    stat, p_value = stats.shapiro(data)
    alpha = 0.05
    if p_value > alpha:
       return "データは正規分布に従うと仮定できます（帰無仮説を棄却できません）。"
    else:
        return "データは正規分布に従わないと仮定できます（帰無仮説を棄却します）。"

