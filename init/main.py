import csv


def procces_sales_data(file_path):
    total_transactions = 0
    total_revenue = 0
    transaction_by_category = {}

    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f)

        for row in csv_reader:
            try:
                total_amount = float(row[6])
            except ValueError:
                total_amount = 0
            try:
                total_transactions += 1
            except ValueError:
                total_transactions = 0


            total_revenue += total_amount


            category = row[9]
            transaction_by_category[category] = transaction_by_category.get(category, 0) + 1

    average_transaction_amount = total_revenue / total_transactions
    average_transaction_amount = round(average_transaction_amount, 2)


    return {
        'total_transactions': total_transactions,
        'total_revenue': total_revenue,
        'average_transaction_amount': average_transaction_amount,
        'transaction_by_category': transaction_by_category
    }

file_path = r'D:\PYTHON-PROJECTS\database_project\database_project.csv'
result = procces_sales_data(file_path)


print(f"Total transactions: {result['total_transactions']}")
print(f"Total revenue: {result['total_revenue']}")
print(f"Average transaction amount: {result['average_transaction_amount']}")
print("Transactions by category:")
for category, count in result['transaction_by_category'].items():
    print(f"{category}: {count}")