# Create age groups
bins = [0, 18, 25, 35, 45, 60, float('inf')]

labels = [
    '0-18',
    '19-25',
    '26-35',
    '36-45',
    '46-60',
    '60+'
]

df['age_group'] = pd.cut(
    df['age'],
    bins=bins,
    labels=labels,
    include_lowest=True
)
df.head()

# Number of customers
number_of_customer = (
    df.groupby('age_group')['customer_id'].nunique()
)
# Total spending
total_spending = (
    df.groupby('age_group')['revenue'].sum()
)
# Average spending
avg_spending = (
    df.groupby('age_group')['revenue'].mean()
)

# Most purchased category
most_purchased_category = (
    df.groupby('age_group')['category'].agg(lambda x: x.value_counts().idxmax())
)
# Preferred payment method
preferred_method = (
    df.groupby('age_group')['payment_method'].agg(lambda x: x.value_counts().idxmax())
)
