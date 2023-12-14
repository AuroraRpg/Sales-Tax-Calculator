import os
from datetime import datetime
from Dictionary import *


class SalesTax():
  def get_user_info(self):
    user_state = input("Please enter your state abbriv: ").strip().upper()
    return user_state

  def calc(self, state, items):
    total = 0
    base_price = 0
    taxes = []
    for i in items:
      base = items[i]
      tax = sales_tax_rates[state]
      subtotal = float(base) * tax
      taxes.append(subtotal)
      subtotal = float(base) + subtotal
      total += subtotal
      base_price += float(base)
    return round(total, 2), base_price, taxes

class Store():

  def __init__(self):
    self.items = {}
    self.store = None
    self.number_of_items = 0

  def get_item_count(self):
    self.number_of_items = int(input("How many items are you checking out? "))

  def get_item(self):

    for i in range(1, self.number_of_items+1):
      item = input(f"What is the name of Item {i}? ").title()
      price = input("What the price? $")
      self.items[item] = price
    return self.items

  def get_user_store(self):
   store = input("Please enter the name of the store you are in: ").strip().title()
   return store

class Receipt():
  def get_date(self):
    date = datetime.now()
    day = date.day
    month = date.month
    year = date.year
    
    self.time = f"{date.hour}:{date.minute}"
    self.date = f"{day}/{month}/{year}"
    return self.date, self.time

  def create_receipt(self, store, total, base_price, taxes, items, user_state):
    tax = 0
    item_num = 1
    date, time = self.get_date()
    print(f'{date} | {time}')
    print(user_state)
    print(store)
    print("-------------------------------------------------\n")
    for i in items:
      print(f"Item {item_num}: {i}  ${items[i]}")
     
      print(f" Tax      ${round(taxes[tax], 2)}\n")
     
      tax += 1
      item_num += 1

    print("-------------------------------------------------")
    
    print(f"Subtotal:  ${base_price}")
    tax_total = 0.00
    for i in taxes:
      tax_total += i
    print(f"Total Tax: ${round(tax_total, 2)}")
    print(f"Total: ${total}")
    
  def save_receipt(self, store, total, base_price, taxes, items, user_state):
    tax = 0
    item_num = 1
    date, time = self.get_date()
    with open(f"{store} - {date} {time}.txt") as f:
      f.write(f'{date} | {time}')
      f.write(user_state)
      f.write(store)
      f.write("-------------------------------------------------\n")
      for i in items:
        f.write(f"Item {item_num}: {i}  ${items[i]}")
  
        f.write(f" Tax      ${round(taxes[tax], 2)}\n")
  
        tax += 1
        item_num += 1
  
      f.write("-------------------------------------------------")
  
      f.write(f"Subtotal:  ${base_price}")
      tax_total = 0.00
      for i in taxes:
        tax_total += i
      f.write(f"Total Tax: ${round(tax_total, 2)}")
      f.write(f"Total: ${total}")
    f.close()

store = Store()
st = SalesTax()
receipt = Receipt()

user_state = st.get_user_info()
user_store = store.get_user_store()
store.get_item_count()
items = store.get_item()
total, base_price, taxes = st.calc(user_state, items)
os.system("clear")
receipt.create_receipt(user_store, total, base_price, taxes, items, user_state)
receipt.save_receipt(user_store, total, base_price, taxes, items, user_state)

print("Have a good day :)")

