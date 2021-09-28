import socket

import pandas as pd


def is_ip(addr):
    try:
        socket.inet_aton(addr)
    # legal
    except socket.error:
        return False

    return True


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
