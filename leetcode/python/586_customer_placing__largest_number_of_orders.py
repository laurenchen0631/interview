import pandas as pd

# SELECT customer_number
# FROM Orders
# GROUP BY customer_number
# ORDER BY COUNT(*) DESC
# LIMIT 1;
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number').size().reset_index(name='count')
    orders.sort_values(by='count', ascending=False, inplace=True)
    return orders.head(1)[['customer_number']]