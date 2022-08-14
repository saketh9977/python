import datetime

import pandas as pd

IN_DATA_CSV = '../data/nse-2022-01-to-02.csv'

def cell_transformation(cell_val):
    return datetime.datetime.strptime(cell_val,'%Y-%m-%d')

def multi_col_transformation(row):
    
    num_ = row['Close']-row['Open']
    den_ = row['Open']
    
    return (num_/den_) * 100  

def multi_col_transformation_2(row):
    return row['Date'].strftime('%Y-%m')

def main():
    print("starting...")
    
    df_raw = pd.read_csv(IN_DATA_CSV)

    # select query
    df_subset = df_raw[['Date', 'Open', 'Close']]

    # col transformation
    df_subset['change'] = df_subset.apply(multi_col_transformation, axis=1)
    df_subset['Date'] = df_subset['Date'].apply(cell_transformation)
    df_subset['_month'] = df_subset.apply(multi_col_transformation_2, axis=1)

    # where condition
    df_big_change = df_subset[(df_subset['change'] > 1) | (df_subset['change'] < -1)]

    # aggregation
    df_group = df_big_change.groupby(['_month']).agg({
        'change': ['min', 'max'],
        'Close': ['min', 'max']
    })

    print(df_group)
    # print(df_group.dtypes)

if __name__ == '__main__':
    main()