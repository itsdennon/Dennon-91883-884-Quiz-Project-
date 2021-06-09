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
