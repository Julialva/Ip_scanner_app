import pandas as pd


def format_df(df):
    columns_data = list(df.columns)
    rows_data = df.to_records(index=False)
    return columns_data, rows_data


def list_in_caps(some_list):
    package = []
    for item in some_list:
        if isinstance(item, str):
            package.append(item.upper())
        else:
            package.append(item)
    return package
