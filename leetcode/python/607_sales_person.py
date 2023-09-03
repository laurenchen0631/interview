import pandas as pd

# SELECT name
# FROM SalesPerson
# WHERE sales_id NOT IN (
    # SELECT sales_id
    # FROM Orders
    # JOIN Company c ON c.com_id = Orders.com_id
    # WHERE c.name = 'RED'
# )
def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    com_order = pd.merge(company, orders, on='com_id')
    red_orders = com_order[com_order['name'] == 'RED'].sales_id.unique()
    valid_sales = sales_person[~sales_person['sales_id'].isin(red_orders)]
    return valid_sales[['name']]
    