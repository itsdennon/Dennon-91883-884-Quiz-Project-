while True:
    name = input("May I please know your name? : ")   #Here is where I ask the user for their name
    print("------------------------------")
    if name.isalpha():
        break
    print("Please enter letters only.")       

while True:
    age = input("Please tell me your age? : ")    #Here is where I ask the user for their age
    print("------------------------------")
    if age.isnumeric():
        break
    print("Please enter numbers only.")

while True:
    yearlvl = input("And lastly, what is your year level? : ")      #Here is where I ask the user for their year level
    print("------------------------------")
    if yearlvl.isnumeric():
        break
    print("Please enter numbers only.")
