def age_group_classifier (age):

    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age>= 20  and age <=40:
        return "adults"
    else:
        return "adults"

def main():

  age = int(input("Enter your age: ")) 
  # Get the user's age
  group = age_group_classifier(age)
   # Call the function to classify the age group
  print("You belong to the age group:", group) 
  # Print the result
if __name__ == "__main__":
  main()

    




