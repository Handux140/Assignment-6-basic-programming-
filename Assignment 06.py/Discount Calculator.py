def discount_calculator(purchase_amount):
  if purchase_amount > 100:
    return 0.1
  elif purchase_amount > 50 and purchase_amount <= 100:
    return 0.05
  elif  purchase_amount <= 50:
    return 0.0
  else:
    return 0.0

def main():
  
  purchase_amount = float(input("Enter the purchase amount: "))
  discount = discount_calculator(purchase_amount)
  discounted_amount = purchase_amount * (1 - discount)
  print("Discounted amount: ", discounted_amount)

if __name__ == "__main__":
  main()
  