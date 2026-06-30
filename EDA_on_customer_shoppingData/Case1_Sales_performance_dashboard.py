import numpy as np
import pandas as pd

df = pd.read_csv('customer_shopping_data.csv')
df.head()
df.info()
df.describe()

# Find missing values.

df.isnull().sum()

# Remove duplicates.

df.duplicated().sum()

# Convert invoice_date to a datetime type.
df['invoice_date'] = pd.to_datetime(df['invoice_date'])
df.info()
# Create a new column: Revenue
df['revenue'] = df['quantity'] * df['price']
df.head()
# Total Revenue
total_revenue = df['revenue'].sum()
print(total_revenue)

# Total Orders
total_orders = df['invoice_no'].nunique()
print(total_orders)

# Total Customers
total_customers = df['customer_id'].nunique()
print(total_customers)

# Average Order Value
average_order_value = total_revenue/total_orders
print(average_order_value)
# Revenue by Category
revenue_by_category=(
df.groupby('category')['revenue'].sum()
)

# Revenue by Shopping Mall
revenue_by_mall=(
df.groupby('shopping_mall')['revenue'].sum()
)
# Revenue by Payment Method
revenue_by_payment=(
df.groupby('payment_method')['revenue'].sum()
)
# Monthly Revenue Trend
monthly_revenue = (
    df.groupby(df['invoice_date'].dt.month)['revenue']
      .sum()
)

print(monthly_revenue)


# Dashboard Visualization

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize=(14,10))
revenue_by_category.plot(
    kind='bar',
    ax=ax[0,0]
)

ax[0,0].set_title("Revenue by Category")

revenue_by_mall.plot(
    kind='bar',
    ax=ax[0,1]
)

ax[0,1].set_title("Revenue by Shopping Mall")

monthly_revenue.plot(
    kind='line',
    marker='o',
    ax=ax[1,0]
)

ax[1,0].set_title("Monthly Revenue Trend")

revenue_by_payment.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax[1,1]
)

ax[1,1].set_title("Revenue by Payment Method")

plt.tight_layout()
