import matplotlib.pyplot as plt
import pandas as pd

# Hypothetical bank statement data with similar descriptions
bank_statement = [
    {'date': '2024-05-01', 'description': 'GROCERY STORE', 'amount': -50.00},
    {'date': '2024-05-03', 'description': 'RESTAURANT', 'amount': -30.00},
    {'date': '2024-05-05', 'description': 'GAS STATION', 'amount': -40.00},
    {'date': '2024-05-10', 'description': 'ELECTRIC COMPANY', 'amount': -100.00},
    {'date': '2024-05-15', 'description': 'CLOTHING STORE', 'amount': -80.00},
    {'date': '2024-05-20', 'description': 'GROCERY STORE', 'amount': -70.00},
    {'date': '2024-05-25', 'description': 'RESTAURANT', 'amount': -45.00}
]

# Convert bank statement data to a DataFrame
df = pd.DataFrame(bank_statement)

# Group transactions by description and sum the amounts
transactions = df.groupby('description').agg({'date': 'count', 'amount': 'sum'})

# Create a bar graph
plt.bar(transactions.index, transactions['amount'], color='skyblue')

# Adding labels and title
plt.xlabel('Transaction Categories')
plt.ylabel('Amount ($)')
plt.title('Monthly Transactions')

# Adding date labels
for i, amount in enumerate(transactions['amount']):
    plt.text(i, amount + 5, f"{transactions['date'][i]} transactions", ha='center')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()
plt.show()
