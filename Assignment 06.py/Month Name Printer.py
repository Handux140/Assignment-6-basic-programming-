def print_month_name():

  Months= ["January", "February", "March", "April", "May", "June", "July", "August", 
         "September", "October", "November", "December"]

  month_num = int(input("Enter a month number: "))
  if month_num < 1 or month_num > 12:
    print("Invalid month number")
  else:
    print(Months[month_num - 1])
    

def main():
  print_month_name()

main()