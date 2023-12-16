import tkinter as tk
from tkinter import ttk
from src.features.build_features import validate_origin_destination

from src.models.predict_model import predict
def main():
    root = tk.Tk()
    root.geometry("500x400")
    root.title("Prédiction du prix du billet")

    date_frame = ttk.Frame(root)
    date_frame.pack(pady=10)

    day_frame = ttk.Frame(date_frame)
    day_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    days = list(range(1, 32)) 
    day_var = tk.StringVar()
    day_label = ttk.Label(day_frame, text="Jour de départ")
    day_label.pack(side=tk.TOP)
    day_combobox = ttk.Combobox(day_frame, values=days, textvariable=day_var)
    day_combobox.pack(side=tk.BOTTOM)
    day_combobox.config(justify='center')

    month_frame = ttk.Frame(date_frame)
    month_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    months = list(range(1, 13)) 
    month_var = tk.StringVar()
    month_label = ttk.Label(month_frame, text="Mois de départ")
    month_label.pack(side=tk.TOP)
    month_combobox = ttk.Combobox(month_frame, values=months, textvariable=month_var)
    month_combobox.pack(side=tk.BOTTOM)
    month_combobox.config(justify='center')

    year_frame = ttk.Frame(date_frame)
    year_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    years = list(range(2023, 2033)) 
    year_var = tk.StringVar()
    year_label = ttk.Label(year_frame, text="Année de départ")
    year_label.pack(side=tk.TOP)
    year_combobox = ttk.Combobox(year_frame, values=years, textvariable=year_var)
    year_combobox.pack(side=tk.BOTTOM)
    year_combobox.config(justify='center')

    horaire_frame = ttk.Frame(root)
    horaire_frame.pack(pady=10)

    hour_frame = ttk.Frame(horaire_frame)
    hour_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    hours = list(range(5, 23)) 
    hour_var = tk.StringVar()
    hour_label = ttk.Label(hour_frame, text="Heure de départ")
    hour_label.pack(side=tk.TOP)
    hour_combobox = ttk.Combobox(hour_frame, values=hours, textvariable=hour_var)
    hour_combobox.pack(side=tk.BOTTOM)
    hour_combobox.config(justify='center')

    min_frame = ttk.Frame(horaire_frame)
    min_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    minutes = list(range(0, 60, 5))
    minute_var = tk.StringVar()
    min_label = ttk.Label(min_frame, text="Minute de départ")
    min_label.pack(side=tk.TOP)
    minute_combobox = ttk.Combobox(min_frame, values=minutes, textvariable=minute_var)
    minute_combobox.pack(side=tk.BOTTOM)
    minute_combobox.config(justify='center')

    trajet_frame = ttk.Frame(root)
    trajet_frame.pack(pady=10)

    origin_frame = ttk.Frame(trajet_frame)
    origin_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    origin_var = tk.StringVar()
    origin_label = ttk.Label(origin_frame, text="Origine")
    origin_label.pack(side=tk.TOP)
    origin_options = ['MADRID', 'BARCELONA', 'PONFERRADA', 'SEVILLA', 'VALENCIA']
    origin_combobox = ttk.Combobox(origin_frame, values=origin_options, textvariable=origin_var)
    origin_combobox.pack(side=tk.BOTTOM)
    origin_combobox.config(justify='center')


    dest_frame = ttk.Frame(trajet_frame)
    dest_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    destination_var = tk.StringVar()
    destination_label = ttk.Label(dest_frame, text="Destination")
    destination_label.pack(side=tk.TOP)
    destination_options = ['MADRID', 'BARCELONA', 'PONFERRADA', 'SEVILLA', 'VALENCIA']
    destination_combobox = ttk.Combobox(dest_frame, values=destination_options, textvariable=destination_var)
    destination_combobox.pack(side=tk.BOTTOM)
    destination_combobox.config(justify='center')

    origin_var.trace_add('write', validate_origin_destination)
    destination_var.trace_add('write', validate_origin_destination)

    type_class_tarif_frame = ttk.Frame(root)
    type_class_tarif_frame.pack(pady=10)

    type_frame = ttk.Frame(type_class_tarif_frame)
    type_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    train_type_var = tk.StringVar()
    train_type_label = ttk.Label(type_frame, text="Type de train")
    train_type_label.pack(side=tk.TOP)
    train_type_options = ['ALVIA','AV City', 'AVE', 'AVE-LD', 'AVE-MD', 'AVE-TGV', 'INTERCITY', 'LD', 'LD-AVE', 'LD-MD', 'MD', 'MD-AVE', 'MD-LD', 'R. EXPRES', 'REGIONAL', 'TRENHOTEL']
    train_type_combobox = ttk.Combobox(type_frame, values=train_type_options, textvariable=train_type_var)
    train_type_combobox.pack(side=tk.BOTTOM)
    train_type_combobox.config(justify='center')

    class_frame = ttk.Frame(type_class_tarif_frame)
    class_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    train_class_var = tk.StringVar()
    train_class_label = ttk.Label(class_frame, text="Classe de train")
    train_class_label.pack(side=tk.TOP)
    train_class_options = ['Touriste avec couchette','Préférentiel', 'Touriste', 'Touriste Plus', 'Touriste avec lien']
    train_class_combobox = ttk.Combobox(class_frame, values=train_class_options, textvariable=train_class_var)
    train_class_combobox.pack(side=tk.BOTTOM)
    train_class_combobox.config(justify='center')

    tarif_frame = ttk.Frame(type_class_tarif_frame)
    tarif_frame.pack(side=tk.LEFT, pady=5, fill=tk.BOTH, expand=True)
    fare_var = tk.StringVar()
    fare_label = ttk.Label(tarif_frame, text="Tarif")
    fare_label.pack(side=tk.TOP)
    fare_options = ['Adulte seul','Flexible', 'Groupe', 'Promo', 'Promo +']
    fare_combobox = ttk.Combobox(tarif_frame, values=fare_options, textvariable=fare_var)
    fare_combobox.pack(side=tk.BOTTOM)
    fare_combobox.config(justify='center')

    spacer_frame = ttk.Frame(type_class_tarif_frame, height=10) 
    spacer_frame.pack()

    predict_button = ttk.Button(root, text="Prédire", command=predict)
    predict_button.pack()

    result_frame = ttk.Frame(root, padding=(10, 10, 10, 0))
    result_frame.pack()

    prediction_label = ttk.Label(result_frame, text="")
    prediction_label.pack()

    root.mainloop()