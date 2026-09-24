import pandas as pd
import os


def data_cleaning(input_file, date_columns=None, outlier_columns=None):
    
    df = pd.read_csv(
        input_file,
        na_values=['', ' ', 'NA', 'N/A', 'null', 'NULL', '?', 'None'],
        parse_dates=date_columns
    )
    df.columns = df.columns.str.strip().str.lower()

    rows_start = len(df)
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]

    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(0)


    if date_columns:
        print(f"{input_file} date types:")
        print(df[date_columns].dtypes)


    dups = df.duplicated().sum()
    df = df.drop_duplicates()

    outliers_removed = {}
    if outlier_columns:
        for col in outlier_columns:
            if col not in df.columns:
                continue

            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            mask = (df[col] < lower) | (df[col] > upper)
            outliers_removed[col] = int(mask.sum())
            df = df[~mask]

    print(f"\n{input_file}: {rows_start} -> {len(df)} rows "
          f"(dups removed: {dups}, outliers removed: {outliers_removed})")
    if len(nulls) > 0:
        print(f"  nulls: {nulls.to_dict()}")


    return df



if __name__ == '__main__':

    files_config = {
        'customers_dataset.csv': {'date_columns': None, 'outlier_columns': []},
        'geolocation_dataset.csv': {'date_columns': None, 'outlier_columns': []},
        'orders_dataset.csv': {
            'date_columns': [
                'order_purchase_timestamp', 'order_approved_at',
                'order_delivered_carrier_date', 'order_delivered_customer_date',
                'order_estimated_delivery_date'
            ],
            'outlier_columns': []
        },
        'order_items_dataset.csv': {'date_columns': ['shipping_limit_date'], 'outlier_columns': []},
        'order_payments_dataset.csv': {'date_columns': None, 'outlier_columns': []},
        'order_reviews_dataset.csv': {
            'date_columns': ['review_creation_date', 'review_answer_timestamp'],
            'outlier_columns': []
        },
        'products_dataset.csv': {'date_columns': None, 'outlier_columns': ['product_weight_g']},
        'product_category_name_translation.csv': {'date_columns': None, 'outlier_columns': []},
        'sellers_dataset.csv': {'date_columns': None, 'outlier_columns': []},
    }

    os.makedirs('cleaned', exist_ok=True)

    for file, config in files_config.items():
        cleaned_df = data_cleaning(file, **config)
        name, ext = os.path.splitext(file)
        cleaned_df.to_csv(os.path.join('cleaned', f"{name}_cleaned{ext}"), index=False)


df2 = pd.read_csv('geolocation_dataset.csv')
print(df2.dtypes)