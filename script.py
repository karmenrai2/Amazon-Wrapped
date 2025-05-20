import pandas as pd 

orderHistory = pd.read_csv('Retail.OrderHistory.1.csv')
orderHistory.drop(columns=['Shipping Address', 'Billing Address', 'Gift Sender Name', 'Gift Recipient Contact Details'])
print(orderHistory.to_string())
print(orderHistory.info())

totalSpent = orderHistory['Total Owed'].sum()
print(totalSpent)
maxPurchase = orderHistory['Product Name'].iloc[orderHistory['Total Owed'].idxmax()]
minPurchase = orderHistory['Product Name'].iloc[orderHistory['Total Owed'].idxmin()]
print(maxPurchase)
print(minPurchase)
totalShipping = orderHistory['Shipping Charge'].sum()
print(totalShipping)
percentageShipping = int(round((totalShipping / totalSpent) * 100)) 
print(str(percentageShipping) + '%')