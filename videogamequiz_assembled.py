#Dennon's Quiz


score = 0 #This is the quiz score
print("******************************")             #Quiz introduction
print("Welcome to my Video Game Quiz!")
print("******************************")
print()
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
    
# **** Main routine *****
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

from random import shuffle

def rounds():
    global r , total                                      #This is the round mechanics
    while True:
        try:                                              
            r = int(input("\nThis quiz has a maximum of 5 rounds, how many questions would you like? Please choose from 1 - 5 : "))
            if 0<r<=5: 
                break
            else:
                print("Please enter the rounds in 1-5 only")
        except:
            print('Please enter rounds in numbers only (The max is 5)')
            

    
        
    total=r

    
rounds()
print()
instructions()
#Using dictionary for the question and the right answer to them
vgquiz =[
[
    "What was Minecrafts release date?",
    {'answer':'a','option':'a)18 November 2011\nb)24 October 2010\nc)09 May 2012\n'}   #These are the questions which will be in the quiz
    ],
[
    "When was the first video game created?",
    {'answer':'a','option':'a)October 1958\nb)November 1972\nc)January 1950\n'}
    ],
[
    "What is the best selling console of all time?",
    {'answer':'c','option':'a)Nintendo 64\nb)Xbox One\nc)Playstation 2\n'}
    ],
[
    "What is the dimension that consists of Ghasts?",
    {'answer':'b','option':'a)The End\nb)The Nether\nc)The Other\n'}
    ],
[
    "Approximately how many people around the world play video games?",
    {'answer':'c','option':'a)2.1 Billion\nb)5.3 Billion\nc)3.1 billion\n'}
    ]
]


shuffle(vgquiz)       #The quiz will use shuffle to display the questions randomly


while r>0:
    data = vgquiz[0]
    q = data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print("----------------------------------------------------------------------")
    print(q)
    print(option)                                                                           #This is how the quiz will display the questions
    while True:
        user_answer = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answer == 'a' or user_answer == 'b'or user_answer == 'c':
            if user_answer == answer:
                print("Correct!")
                print("Score : ",)
                print("\n")
                score +=1                       #This is how the quiz will function if the user gets the answer correct
                print("================")
                print("Your score is",score)
                print("================")
            else:
                print("Sorry, your answer is incorrect")
                print("The answer is",answer)
                print("\n")
                print("================")                 #This is how the quiz will function if the user gets the answer incorrect
                print("Your score is",score)
                print("================")
              

            del vgquiz[0]
            r-=1
            break
        else:                                                     #This is how the quiz will function if the user enters an improper answer
            print("Please enter your answer in a,b,c only")
            print()

#FINAL MESSAGE
print("******************************")
print("Thank you for playing my Quiz!")  #This is the conclusion of the quiz
print("Nice work, your total score is:", score,)   #The quiz will show the user their final score here
print("******************************")
print("By Dennon Fernando 11CSC")
print("==============================")

    
