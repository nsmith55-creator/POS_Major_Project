import os
total = float(0)
subtotal = float(0)
pay_made = float(0)
discount = float(0)
GCT = float(0.15)
choice = int(0)
cart =[]



store_items=[
    {"name":"Apple", "quantity":50, "price": 150},
    {"name":"Snickers", "quantity":100, "price": 450},
    {"name":"Red Stripe", "quantity":100, "price": 500},
    {"name":"AAA Battery", "quantity":200, "price": 200},
    {"name":"Paper Plate (50 per pack)", "quantity":1000, "price": 250},
    {"name":"Gatorade", "quantity":230, "price": 150},
    {"name":"Canada Dry", "quantity":200, "price": 170},
    {"name":"Popcorn", "quantity":33, "price": 100},
    {"name":"Chocolate Ice Cream", "quantity":300, "price": 750},
    {"name":"Sliced Cheese", "quantity":90, "price": 320},
    {"name":"Cinamon Role", "quantity":100, "price": 80},
]

def main():
  os.system('cls')
  menu_options()
  

def prod_list():
  print(f"{'Product':<25} {'Quantity':<10} {'Price':<10}")
  for item in store_items:
    print(f"{item['name']:<25} {item['quantity']:<10} ${item['price']:<10}")


def choice_validation(choice_made):
  if choice_made <1 or choice_made >4:
    os.system('cls')
    print("The option you select can only be from 1-4 please try again")
    menu_options()
    return 0


def menu_options():
  print("Welcome to Best Buy Retail Store POS")
  print("-----------------------------------------")
  print("")
  print("Please select an option below")
  print("1. Add item to cart")
  print("2. Remove item from cart")
  print("3. View Cart")
  print("4. Close Program")
  choice = int(input("Enter your choice by number here: " ))
  choice_validation(choice)
  choices(choice)
  

def choices(choice_selected):
  match choice_selected:
    case 1:
      add_to_cart()

  
def add_to_cart():
  item_name =""
  while item_name !="0":
    prod_list()
    print("--------------------------------")
    print("Enter 0 to return to main menu")
    item_name = input("Enter the name of the product you wish to add to cart: ")
    if item_name == "0":
      os.system('cls')
      menu_options()
    else:
      quantity = input("Enter the quantity: ")
      for item in store_items:
        if item["name"] == item_name:
          print(item_name)

main()