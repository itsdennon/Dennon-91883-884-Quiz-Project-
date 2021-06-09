from random import shuffle
index = 0
score = 0
optnum = 0


def rounds():
    global r , total
    while True:
        try:
            r = int(input("\nPlease enter how many rounds do you want to play there are a total of 20 round at max. : "))
            if 0<r<=20: 
                break
            else:
                print("Please enter the rounds in 1-20 only")
        except:
            print('Please enter rounds in numbers only (The max is 20)')
            

    
        
    total=r

    



rounds()

#using dictionary for the question and the right answer to them
vgquiz =[
[
    "What was Minecrafts release date?",
    {'answer':'a','option':'a)18 November 2011\nb)24 October 2010\nc)09 May 2012\nd)24 October 2010\n'}
    ],
[
    "When was the first video game created?",
    {'answer':'a','option':'a)October 1958\nb)November 1972\nc)January 1950\nd)24 October 2010\n'}
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

shuffle(vgquiz)


while r>0:
    data = vgquiz[0]
    q = data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answer = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answer == 'a' or user_answer == 'b'or user_answer == 'c':
            if user_answer == answer:
                print("Correct!")
                print("Score : ",)
                print("\n")
                score +=1 
                print("================")
                print("Your score is",score)
                print("================")
            else:
                print("Sorry, your answer is incorrect")
                print("The answer is",answer)
                print("\n")

            del vgquiz[0]
            r-=1
            break
        else:
            print("Please enter your answer in a,b,c only")
