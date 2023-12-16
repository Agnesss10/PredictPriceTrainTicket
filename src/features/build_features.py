from warnings import showwarning
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def analyse_corr(data):
    sns.heatmap(data.corr())
    plt.savefig('../reports/figures/correlation_map.png')
    
    
def split_data(data, category):
    selected_data = data[data['price_category'] == category]
    X = selected_data.drop(columns=['price', 'price_category'], axis=1) 
    y = selected_data['price']
    return train_test_split(X, y, test_size=0.2)

def show_metrics(y_test, y_pred):
    print('R² = ', r2_score(y_test, y_pred))
    MSE = mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(MSE)
    print('MSE = ', MSE)
    print('RMSE = ',RMSE)
    
def validate_origin_destination(*args):
    origin = origin_var.get()
    destination = destination_var.get()
    
    if origin == destination:
        destination_var.set('')
        showwarning('Attention', 'Les champs Origine et Destination ne peuvent pas avoir la même valeur.')