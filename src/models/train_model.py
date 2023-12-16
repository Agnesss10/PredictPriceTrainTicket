from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor  
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def train_random_forest_classifier(X_train, y_train, n_estimators, max_depth):    
    rf_clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    rf_clf.fit(X_train, y_train)
    return rf_clf


def train_linear_regression(X_train, y_train):   
   lr = LinearRegression()
   lr.fit(X_train, y_train)
   return lr
   

def train_cart(X_train, y_train):   
   cart = DecisionTreeRegressor()  
   cart.fit(X_train, y_train)
   return cart

   
def train_random_forest_regressor(X_train, y_train):   
    rf_reg = RandomForestRegressor()
    rf_reg.fit(X_train, y_train)
    return rf_reg