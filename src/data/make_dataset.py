# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path

import pandas as pd
from dotenv import find_dotenv, load_dotenv

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
        

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()

def load_raw_data():
    data = pd.read_csv('../data/raw/DataSet.csv', sep=',') 
    return data

def load_processed_data():
    data = pd.read_csv('../data/processed/final.csv', sep=',') 
    return data

def modify_column(data, column, col):
    if col == 'day':
        data['Dep_day'] = pd.to_datetime(data[column], format='%Y-%m-%d %H:%M:%S').dt.day
    elif col == 'month':
        data['Dep_month'] = pd.to_datetime(data[column], format='%Y-%m-%d %H:%M:%S').dt.month
    elif col == 'year':
        data['Dep_year'] = pd.to_datetime(data[column], format='%Y-%m-%d %H:%M:%S').dt.year
    elif col == 'hour':
        data['Dep_hour'] = pd.to_datetime(data[column], format='%Y-%m-%d %H:%M:%S').dt.hour
    elif col == 'minute':
        data['Dep_minute'] = pd.to_datetime(data[column], format='%Y-%m-%d %H:%M:%S').dt.minute
    else:
        raise ValueError("Invalid 'col' argument. Use 'day', 'month', 'year', 'hour', or 'minute'.")


def clean_data(data):
    data = data.drop(columns=['Unnamed', 'insert_date'])
    data.insert(0,'price',data.pop('price'))
    data = data.dropna() 
    return data

def process_data(data): 
    modify_column(data, 'start_date', 'day')
    modify_column(data, 'start_date', 'month')
    modify_column(data, 'start_date', 'year')
    modify_column(data, 'start_date', 'hour')
    modify_column(data, 'start_date', 'minute')
    
    data = data.drop(columns=['start_date', 'end_date'])
    
    data_pre = pd.get_dummies(data.iloc[:,[1,2,3,4,5]])
    df = pd.concat([data, data_pre], axis=1)
    df = df.drop(columns=['origin','destination','train_type','train_class','fare'], axis=1)
    
    df.to_csv('../data/processed/final.csv', index=False)
    return df