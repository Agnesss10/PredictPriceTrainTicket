from turtle import pd
from sklearn.metrics import accuracy_score

def predict_rf_classification(rf_clf_model, X_test):
    y_pred = rf_clf_model.predict(X_test)
    return y_pred

def predict_linear_regression(lr_model, X_test):
    y_pred = lr_model.predict(X_test)
    return y_pred 

def predict_cart(cart_model, X_test):
    y_pred = cart_model.predict(X_test)
    return y_pred

def predict_rf_regressor(rf_reg_model, X_test):
    y_pred = rf_reg_model.predict(X_test)
    return y_pred

def accuracy(y_test, predictions):
    return accuracy_score(y_test, predictions)

def predict_price(features_input, features, model):
    # Convertir les entrées utilisateur en DataFrame
    input_df = pd.DataFrame([features_input], columns=features.columns)
    
    # Colonnes date & heure
    input_df['Dep_day'] = features_input['Dep_day']
    input_df['Dep_month'] = features_input['Dep_month']
    input_df['Dep_year'] = features_input['Dep_year']
    input_df['Dep_hour'] = features_input['Dep_hour']
    input_df['Dep_min'] = features_input['Dep_min']
    
    # Colonnes origin
    input_df['origin_MADRID'] = features_input['origin_MADRID'] 
    input_df['origin_PONFERRADA'] = features_input['origin_PONFERRADA']
    input_df['origin_SEVILLA'] = features_input['origin_SEVILLA']
    input_df['origin_VALENCIA'] = features_input['origin_VALENCIA']

    # Colonnes destination
    input_df['destination_MADRID'] = features_input['destination_MADRID']
    input_df['destination_PONFERRADA'] = features_input['destination_PONFERRADA']
    input_df['destination_SEVILLA'] = features_input['destination_SEVILLA']
    input_df['destination_VALENCIA'] = features_input['destination_VALENCIA']
    
    # Colonnes type
    input_df['train_type_ALVIA'] = features_input['train_type_ALVIA']
    input_df['train_type_AV City'] = features_input['train_type_AV City']
    input_df['train_type_AVE'] = features_input['train_type_AVE'] 
    input_df['train_type_AVE-LD'] = features_input['train_type_AVE-LD']
    input_df['train_type_AVE-MD'] = features_input['train_type_AVE-MD']
    input_df['train_type_AVE-TGV'] = features_input['train_type_AVE-TGV']
    input_df['train_type_INTERCITY'] = features_input['train_type_INTERCITY']
    input_df['train_type_LD'] = features_input['train_type_LD']
    input_df['train_type_LD-AVE'] = features_input['train_type_LD-AVE']  
    input_df['train_type_LD-MD'] = features_input['train_type_LD-MD']
    input_df['train_type_MD'] = features_input['train_type_MD']
    input_df['train_type_MD-AVE'] = features_input['train_type_MD-AVE'] 
    input_df['train_type_MD-LD'] = features_input['train_type_MD-LD']
    input_df['train_type_R. EXPRES'] = features_input['train_type_R. EXPRES']  
    input_df['train_type_REGIONAL'] = features_input['train_type_REGIONAL']
    input_df['train_type_TRENHOTEL'] = features_input['train_type_TRENHOTEL']
    
    # Colonnes class
    input_df['train_class_Cama Turista'] = features_input['train_class_Cama Turista']
    input_df['train_class_Preferente'] = features_input['train_class_Preferente']
    input_df['train_class_Turista'] = features_input['train_class_Turista']
    input_df['train_class_Turista Plus'] = features_input['train_class_Turista Plus']  
    input_df['train_class_Turista con enlace'] = features_input['train_class_Turista con enlace']

    # Colonnes fare  
    input_df['fare_Adulto ida'] = features_input['fare_Adulto ida']
    input_df['fare_Flexible'] = features_input['fare_Flexible']
    input_df['fare_Mesa'] = features_input['fare_Mesa'] 
    input_df['fare_Promo'] = features_input['fare_Promo']
    input_df['fare_Promo +'] = features_input['fare_Promo +']

    
    # Faire la prédiction
    predicted_price = model.predict(input_df)
    return predicted_price[0]

def predict():
    features_input = {
        'Dep_day': int(day_var.get()),
        'Dep_month': int(month_var.get()),
        'Dep_year': int(year_var.get()),
        'Dep_hour': int(hour_var.get()),
        'Dep_min': int(minute_var.get()),
        'origin_MADRID': True if origin_var.get() == "MADRID" else False,
        'origin_BARCELONA': True if origin_var.get() == "BARCELONA" else False,
        'origin_PONFERRADA': True if origin_var.get() == "PONFERRADA" else False,
        'origin_SEVILLA': True if origin_var.get() == "SEVILLA" else False, 
        'origin_VALENCIA': True if origin_var.get() == "VALENCIA" else False,
        'destination_MADRID': True if destination_var.get() == "MADRID" else False,
        'destination_BARCELONA': True if destination_var.get() == "BARCELONA" else False,
        'destination_PONFERRADA': True if destination_var.get() == "PONFERRADA" else False,
        'destination_SEVILLA': True if destination_var.get() == "SEVILLA" else False, 
        'destination_VALENCIA': True if destination_var.get() == "VALENCIA" else False,
        'train_type_ALVIA': True if train_type_var.get() == "ALVIA" else False,
        'train_type_AV City': True if train_type_var.get() == "AV City" else False,
        'train_type_AVE': True if train_type_var.get() == "AVE" else False,
        'train_type_AVE-LD': True if train_type_var.get() == "AVE-LD" else False,
        'train_type_AVE-MD': True if train_type_var.get() == "AVE-MD" else False,
        'train_type_AVE-TGV': True if train_type_var.get() == "AVE-TGV" else False,
        'train_type_INTERCITY': True if train_type_var.get() == "INTERCITY" else False,
        'train_type_LD': True if train_type_var.get() == "LD" else False,
        'train_type_LD-AVE': True if train_type_var.get() == "LD-AVE" else False,
        'train_type_LD-MD': True if train_type_var.get() == "LD-MD" else False,
        'train_type_MD': True if train_type_var.get() == "MD" else False,
        'train_type_MD-AVE': True if train_type_var.get() == "MD-AVE" else False,
        'train_type_MD-LD': True if train_type_var.get() == "MD-LD" else False,
        'train_type_R. EXPRES': True if train_type_var.get() == "R. EXPRES" else False,
        'train_type_REGIONAL': True if train_type_var.get() == "REGIONAL" else False,
        'train_type_TRENHOTEL': True if train_type_var.get() == "TRENHOTEL" else False,
        'train_class_Cama Turista': True if train_class_var.get() == "Touriste avec couchette" else False,
        'train_class_Preferente': True if train_class_var.get() == "Préférentiel" else False,
        'train_class_Turista': True if train_class_var.get() == "Touriste" else False,
        'train_class_Turista Plus': True if train_class_var.get() == "Touriste Plus" else False,
        'train_class_Turista con enlace': True if train_class_var.get() == "Touriste avec lien" else False,
        'fare_Adulto ida': True if fare_var.get() == "Adulte seul" else False,
        'fare_Flexible': True if fare_var.get() == "Flexible" else False,
        'fare_Mesa': True if fare_var.get() == "Groupe" else False,
        'fare_Promo': True if fare_var.get() == "Promo" else False,
        'fare_Promo +': True if fare_var.get() == "Promo +" else False,
    }
    predicted = predict_price(features_input)
    if predicted > 0 and predicted < 50:
        prediction_label.config(borderwidth=2, relief="solid", background="green")
    elif predicted >= 50 and predicted < 100:
        prediction_label.config(borderwidth=2, relief="solid", background="yellow")
    else:
        prediction_label.config(borderwidth=2, relief="solid", background="red")
    prediction_label.config(text=f"Prix prédit du billet : {predicted:.2f} €")