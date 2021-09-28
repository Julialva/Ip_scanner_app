import socket

import pandas as pd


def is_ip(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count(".") == 3
    except socket.error:  # not a valid address
        return False

    return True


def is_ip_cidr(address):
    try:
        string = address.split("/")
        if int(string[1]) < 30 and int(string[1]) > 1:
            cidr = True
        if cidr and is_ip(string[0]):
            return True
        else:
            return False
    except:
        return False


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
