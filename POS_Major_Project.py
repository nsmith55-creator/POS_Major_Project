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
    item_found = False
    cart_found = False
    prod_list()
    print("--------------------------------")
    print("Enter 0 to return to main menu")
    item_name = input("Enter the name of the product you wish to add to cart: ")
    if item_name == "0":
      os.system('cls')
      menu_options()
    else:
      for item in store_items:
        if item["name"].lower() == item_name.lower():
          item_found = True
          quantity = int(input("Enter the quantity: "))
          while item["quantity"] < quantity:
            os.system('cls')
            print("Currently we do not have enough items in stock please try again")
            quantity = int(input("Enter the quantity: "))
          item["quantity"] = item["quantity"] - quantity
          for cart_item in cart:
            if cart_item["name"].lower() == item_name.lower():
              cart_found = True
              cart_item["quantity"] += quantity
              item["quantity"] -= quantity
              break
          if cart_found == False:
            cart.append({"name":item["name"], "quantity":quantity, "price": item["price"]})
            item["quantity"] -= quantity
          print(cart)
          input("Enter Enter Key to continue..... .....")
          break
      if item_found == False:
        print("Item is not in our stocks please try again")
        input('Press Enter Key to continue..... ')
        os.system('cls')
        add_to_cart()
  menu_options()

def choices(choice_selected):
  match choice_selected:
    case 2:
      remove_from_cart()

def remove_from_cart():x
  item_name = input("Enter item name to remove: ")
  
  for item in cart:
    if item["name"].lower() == item_name.lower():
      quantity = int(input("Enter quantity to remove: "))
      
      if quantity >= item["quantity"]:
        cart.remove(item)
      else:
        item["quantity"] -= quantity
      
      print("Item updated/removed from cart.")
      input("Press Enter to continue...")
      os.system('cls')
      menu_options()
      return

  print("Item not found in cart.")
  input("Press Enter to continue...")
  os.system('cls')
  menu_options()    

main()
