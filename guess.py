# create by yeouda cohen 
#date 23/07/2021

import random


randomNumber = random.randrange(0, 10, 1);
print(randomNumber)
count = 0
print("hey whats your name ? ")
your_name = input()
print("hey "+ your_name + " chooch number between 1-10")


for count in range(6) :
    

    guess = int(input())
    print("test")
    #print("your guess " + guess +" count "+ count)

    if(guess == randomNumber):# in case the you guess the number
        print("great " + your_name + "you wine in "+ count+1)
   

    elif(count == 6) :
        print("sory " + your_name +"you lost , you post 6 choose ") 
    
    elif(guess > randomNumber ) :
        print("your number is high") 
        
    else :
        print("your nubmer is to low")   
          
