# 1
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

# class Book(Product):
#     def __init__(self, name, price, quantity, author):
#         super().__init__(name, price, quantity)
#         self.author = author

#     def read(self):
#         print(f"Book Name: {self.name}")
#         print(f"Author: {self.author}")
#         print(f"Price: ${self.price}")
#         print(f"Available Quantity: {self.quantity}")


# my_book = Book(name="Python Programming", price=29.99, quantity=50, author="John Doe")

# my_book.read()
# 2
# class Restaurant:
#     def __init__(self, name, cuisine, menu):
#         self.name = name
#         self.cuisine = cuisine
#         self.menu = menu

# class FastFood(Restaurant):
#     def __init__(self, name, cuisine, menu, drive_thru):
#         super().__init__(name, cuisine, menu)
#         self.drive_thru = drive_thru

#     def order(self, dish_name, quantity):
#         if dish_name in self.menu and quantity <= self.menu[dish_name]['quantity']:
#             total_cost = self.menu[dish_name]['price'] * quantity
#             self.menu[dish_name]['quantity'] -= quantity
#             return total_cost
#         elif dish_name not in self.menu:
#             return "Dish not available"
#         else:
#             return "Requested quantity not available"


# menu = {
#     'burger': {'price': 5, 'quantity': 10},
#     'pizza': {'price': 10, 'quantity': 20},
#     'drink': {'price': 1, 'quantity': 15}
# }

# mc = FastFood('McDonalds', 'Fast Food', menu, True)

# print(mc.order('burger', 5))  
# print(mc.order('burger', 15)) 
# print(mc.order('soup', 5))    
