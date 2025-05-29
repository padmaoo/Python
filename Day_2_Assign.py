inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

# Questions
# 1.Calculate the Total Revenue
# 2.List low stock item if stock is less than 5
# 3.Calculte the category-wise Revenue

# Question - 1 
Total_revenue = 0
for item in inventory:
    Total_revenue += item[2] * item[3]
print(f'Total Revenue : ',Total_revenue)
# Output : Total Revenue :  669.0
    
# Question - 2
for item in inventory:
    if item[4] < 5:
        print('Low stock item is : ',item[0])
# Output : Low stock item is :  Cheddar
        # Low stock item is :  Baguette
        # Low stock item is :  Croissant

# Question - 3
Total_revenue_category = 0
for item in inventory:
    Total_revenue_category = item[2] * item[3]
    print(f'Category : {item[1]} , Revenue : {Total_revenue_category : .2f}')
# Output : Category : Fruit , Revenue :  140.00
        # Category : Vegetable , Revenue :  55.00
        # Category : Dairy , Revenue :  90.00
        # Category : Bakery , Revenue :  98.00
        # Category : Fruit , Revenue :  88.00
        # Category : Vegetable , Revenue :  54.00
        # Category : Dairy , Revenue :  60.00
        # Category : Bakery , Revenue :  84.00