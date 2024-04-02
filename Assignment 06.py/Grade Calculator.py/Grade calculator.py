def grade_calculator (score):
  if score >= 90 and score <= 100:
      return 'A, Excellent '
  elif score >= 80 and score < 90:
      return 'B, Very good'
  elif score >= 70 and score < 80:
      return 'C, Good'
  elif score >= 60 and score < 70:
      return 'D, not bad work hard'
  else:
      return 'F, Fail'

def main():

  # get the score from the user
  score = int(input('Enter your score: '))
  print(grade_calculator(score))

# call the main function
main() 
