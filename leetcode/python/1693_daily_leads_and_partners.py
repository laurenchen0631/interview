import pandas as pd

# SELECT 
#   date_id, 
#   make_name,
#   COUNT(DISTINCT lead_id) AS unique_leads,
#   COUNT(DISTINCT partner_id) AS unique_partners
# FROM DailySales;
# GROUP BY date_id, make_name;
def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(['date_id', 'make_name']).agg({
        'lead_id': pd.Series.nunique,
        'partner_id': pd.Series.nunique,
    }).reset_index()
    
    df.rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'}, inplace=True)
    return df