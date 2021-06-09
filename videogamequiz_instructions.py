def instructions():

  first_time = input("Would you like to read the instructions? Please answer Yes or No. ").lower()  #This is where the quiz asks the user if they want instructions

  if first_time != "yes":
      print()
      print("Welcome to Quiz")
     
  
  else:
    print()
    print("******* Quiz Instructions ********")               #This is the quiz instructions for the user if they need it
    print("You will be given a question with a choice of 3 answers.")
    print("Once you are satisfied with an answer, please select it by either entering A, B or C depending on the answer you have chosen.")
    print("The Quiz will then tell you if you're correct and then add it to your score, then the next question will begin.")
    print("**********************************")
    print()

instructions()
