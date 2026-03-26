import os
total = float(0)
subtotal = float(0)
pay_made = float(0)
discount = float(0)
GCT = float(0.15)
choice = int(0)
tax = float(0)
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
    {"name":"Cinnamon Roll", "quantity":100, "price": 80},
]


def main():
  os.system('cls')
  menu_options()
  

def prod_list():
  print(f"{'Product':<25} {'Quantity':<10} {'Price':<10}") # this line is the header of the product list page that gives an additional spacing for appropriate alignment
  for item in store_items:
    print(f"{item['name']:<25} {item['quantity']:<10} ${item['price']:<10}")

# validation to ensure that the user does not select a number that is not on the listed menu options
def choice_validation(choice_made):
  if choice_made <1 or choice_made >5:
    os.system('cls')
    print("The option you select can only be from 1-4 please try again")
    menu_options()
    return 0


def check_stock():
  for item in store_items:
    if item['quantity'] <= 5:
      print(f"{item['name']} is low on stock {item['quantity']} remaining please request more")


# this function allows for the menu options to be displayed to teh user
def menu_options():
  cart =[]
  print("Welcome to Best Buy Retail Store POS")
  print("-----------------------------------------")
  check_stock()
  print("-----------------------------------------")
  print("")
  print("Please select an option below")
  print("1. Add item to cart")
  print("2. Remove item from cart")
  print("3. View Cart")
  print("4. Checkout")
  print("5. Close Program")
  # this while loop holds a try that allows for error handling while simultainiously allows for the user to make another attempt at entry
  while True:
    try:
      choice = int(input("Enter your choice by number here: " ))
      break
    except ValueError:
      print("Only integers are allowed please try again")
  choice_validation(choice)
  choices(choice)
  

# This function handles the users choice based on the menu page
def choices(choice_selected):
  match choice_selected:
    case 1:
      add_to_cart()
    case 2:
      remove_from_cart()
    case 4:
      checkout()
    case 5:
     goodbye()
  

def add_to_cart():
  os.system('cls')
  item_name = ""
  while item_name !="0":
    item_found = False
    cart_found = False
    check_stock()
    prod_list()
    print("--------------------------------")
    print("Enter 0 to return to main menu")
    item_name = input("Enter the name of the product you wish to add to cart: ")
    if item_name == "0":
      os.system('cls') #This ine makes it so the terminal display shows only the new printed values to enure it is clean
      menu_options()
    else:
      for item in store_items: # a loop to read the dictioary list items
        if item["name"].lower() == item_name.lower():
          item_found = True
          while True:
            try:
              quantity = int(input("Enter the quantity: "))
              break
            except ValueError:
              print("Only numbers are accepted please try again")
          while item["quantity"] < quantity:
            os.system('cls')
            print(f"Currently we only have {item['quantity']} items in stock please try again")
            while True:
              try:
                quantity = int(input("Enter the quantity: "))
                break
              except ValueError:
                print("Only numbers are accepted please try again")
          for cart_item in cart:
            if cart_item["name"].lower() == item_name.lower():
              cart_found = True
              cart_item["quantity"] += quantity
              item["quantity"] -= quantity
              os.system('cls')
              break
          if cart_found == False:
            cart.append({"name":item["name"], "quantity":quantity, "price": item["price"]})
            item["quantity"] -= quantity
          input("Press Enter Key to continue..... ")
          os.system('cls')
          break
      if item_found == False:
        print("Item is not in our stocks please try again")
        input('Press Enter Key to continue..... ')
        os.system('cls')
        add_to_cart()



def remove_from_cart():
  item_name = input("Enter item name to remove: ")
  
  for item in cart:
    if item["name"].lower() == item_name.lower():
      while True:
        try:
          quantity = int(input("Enter quantity to remove: "))
          break
        except ValueError:
          print("Quantity can only be a number, please try again")
  
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

def calc_subtotal():
  subtotal = 0
  for cart_item in cart:
    subtotal = subtotal + (cart_item['quantity']*cart_item['price'])
  return subtotal
  

def checkout():
  change = float(0)
  pay = float(0)
  item_total = float(0)
  subtotal = calc_subtotal()
  discount = float(0.12)
  discounted_price = subtotal * discount
  if subtotal > 5000:
    total = subtotal - discounted_price # total is used to hold the cost after teh discount
    tax = total * 0.10
    final_total = total + tax #final_total stores the cost after tax is applied
  else:
    tax = subtotal * 0.10
    final_total = subtotal+tax
  os.system('cls')
  if cart == []:
    print("There are no items currently in the cart")
    input("Press Enter to return to main menu")
    main()
  print(f"{'Item':<13} {'Quantity':<13} {'Unit Price':<13} {'Item Total'}")
  for item in cart:
    item_total = item['quantity'] * item['price']
    print(f"{item['name']:<13} {item['quantity']:<13} ${item['price']:<13}${item_total}")
  print(f"{'Subtotal:':<41}" ,"$",subtotal)
  if subtotal > 5000:
    print(f"{'Discount(%):':<41}", discount*100,"%")
    print(f"{'Discounte($):':<41}","$",discounted_price)
    print(f"{'Discounted Price:':<41}","$",total)
  print(f"{'Tax (10%):':<41}","$",tax)
  print(f"{'Total:':<41}","$",final_total)
  pay = payment(final_total)
  change = pay - final_total
  os.system('cls')
  print("---------------------------------------------------------------")
  print(f"{'Best Buy Retail Store':<13}")
  print("---------------------------------------------------------------")
  print(f"{'Item':<13} {'Quantity':<13} {'Unit Price':<13} {'Item Total'}")
  for item in cart:
    item_total = item['quantity'] * item['price']
    print(f"{item['name']:<13} {item['quantity']:<13} ${item['price']:<13}${item_total}")
  print(f"{'Subtotal:':<41}" ,"$",subtotal)
  if subtotal > 5000:
    print(f"{'Discount(%):':<41}", discount*100,"%")
    print(f"{'Discounte($):':<41}","$",discounted_price)
    print(f"{'Discounted Price:':<41}","$",total)
  print(f"{'Tax (10%):':<41}","$",tax)
  print(f"{'Total:':<41}","$",final_total)
  print(f"{'Payment:':<41}","$",pay)
  print(f"{'Change:':<41}","$",change)
  print("---------------------------------------------------------------")
  print("Thank you for making it Best Buy Retail Store")
  print("---------------------------------------------------------------")
  input("Press enter to return to main menu")
  cart.clear()
  menu_options()


def payment(total):
  payment = float(0)
  while True:
    try: 
      payment = int(input('Enter the amount paid: ' ))
      break
    except ValueError:
      print("Payment can only be a number, please try again")
  while payment < total:
    print('The amount entered is less than the total value please try entering a value at the same amount or greater')
    while True:
      try: 
        payment = int(input('Enter the amount paid: ' ))
        break
      except ValueError:
        print("Payment can only be a number, please try again")
  return payment


def goodbye():
  print("Thank you for Using Best Buy Retail Store POS")
  return 0

main()