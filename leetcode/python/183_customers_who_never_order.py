import pandas as pd

# SELECT c.name AS Customers 
# FROM Customers c
#   LEFT JOIN Orders o ON c.id = o.customerId
# WHERE o.customerId IS NULL;

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    df = df[df['customerId'].isnull()]
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df