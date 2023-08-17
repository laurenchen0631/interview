import pandas as pd

# SELECT product_id, 'store1' AS Store, store1 AS Price
# FROM Products
# WHERE store1 IS NOT NULL
# UNION
# SELECT product_id, 'store2' AS Store, store2 AS Price
# FROM Products
# WHERE store2 IS NOT NULL
# UNION
# SELECT product_id, 'store3' AS Store, store3 AS Price
# FROM Products
# WHERE store3 IS NOT NULL
 
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    """Rearrange products table."""
    return pd.melt(products, id_vars=['product_id'], value_vars=['store1', 'store2', 'store3'], var_name='Store', value_name='Price').dropna()