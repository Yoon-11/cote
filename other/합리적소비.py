n = int(input())

shopping_list = {}
for _ in range(n):
    name, price = input().split()
    shopping_list[name] = int(price)

max_price, min_price = max(shopping_list.values()), min(shopping_list.values())
max_price_name, min_price_name = '', ''

for name, price in shopping_list.items():
    if price == max(shopping_list.values()):
        max_price_name = name
    if price == min(shopping_list.values()):
        min_price_name = name

print(max_price_name, max_price)
print(min_price_name, min_price)









