import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    res = customers[~customers["id"].isin(orders["customerId"])]
    res = res[["name"]].rename(columns={"name":"Customers"})
    return res