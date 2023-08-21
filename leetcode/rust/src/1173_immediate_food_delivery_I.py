import pandas as pd

# SELECT ROUND(
    # 100 * SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / 
    # COUNT(order_id), 2) AS immediate_percentage
# FROM Delivery
def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'immediate_percentage': [
            round(100 * sum(delivery['order_date'] == delivery['customer_pref_delivery_date']) / len(delivery), 2)
        ]
    })
