import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix

def plot_nb_train_origin(df):
    plt.hist(df["origin"])
    plt.xlabel("Origine")
    plt.ylabel("Nombre")
    plt.savefig("../reports/figures/hist_nb_train_origin.png")
    plt.show()
    
def plot_nb_train_destination(df):
    plt.hist(df["destination"])
    plt.xlabel("Destination")
    plt.ylabel("Nombre") 
    plt.savefig("../reports/figures/hist_nb_train_destination.png")
    plt.show()
    
def plot_nb_train_tarif(df):
    plt.hist(df["fare"])
    plt.xlabel("Tarif")
    plt.ylabel("Nombre") 
    plt.savefig("../reports/figures/hist_nb_train_tarif.png")
    plt.show()
    
def plot_price_distribution(df):
    plt.hist(df["price"])
    plt.xlabel("Price")
    plt.ylabel("Frequency") 
    plt.savefig("../reports/figures/hist_prices.png")
    plt.show()

def matrix_conf(y_test, predictions, y):
    conf_matrix = confusion_matrix(y_test, predictions)
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=sorted(y.unique()), yticklabels=sorted(y.unique()))
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Matrice de Confusion')
    plt.savefig("../reports/figures/conf_matrix.png")
    plt.show()
    

   
def cart_tree(cart_model, max_depth):
    tree.plot_tree(cart_model, max_depth=max_depth)
    plt.savefig("../reports/figures/cart_tree.png")
    plt.show()
    
import numpy as np
import matplotlib.pyplot as plt

def plot_regression(model, y_test, y_pred):
    xmin = np.minimum(y_test.min(), y_pred.min()) - 10
    xmax = np.maximum(y_test.max(), y_pred.max()) + 10
    ymin = np.minimum(y_test.min(), y_pred.min()) - 10
    ymax = np.maximum(y_test.max(), y_pred.max()) + 10
    plt.scatter(y_test, y_pred, marker='+')
    plt.plot([xmin,xmax], [ymin,ymax], lw=1, color='k', ls='--')
    if isinstance(model, RandomForestRegressor):
        plt.savefig("../reports/figures/rf_regressor_plot.png")
        plt.show()
    elif isinstance(model, LinearRegression):
        plt.savefig("../reports/figures/linear_regression_plot.png")
        plt.show()