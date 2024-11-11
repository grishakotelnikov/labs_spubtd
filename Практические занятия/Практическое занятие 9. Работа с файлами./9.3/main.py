import csv

filename = 'products.csv'

total_cost = 0

products = []

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product_name = row['Продукт']
        quantity = int(row['Количество'])
        price = int(row['Цена'])
        total_cost += quantity * price
        products.append((product_name, quantity, price))

print("Нужно купить:")
for product_name, quantity, price in products:
    print(f"{product_name} - {quantity} шт. за {price} руб.")

print(f"Итоговая сумма: {total_cost} руб.")
