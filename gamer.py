import random

win = 0
lost = 0
play = True 

while(play):
   gameBut =["paper","stone","scissors"]

   gamerBut =  (random.choice(gameBut))
   print ("choose paper - stone - scissors ")
   germer = input()
   print(gamerBut)


   if(germer not in gameBut) :
      print("you can Entere only 'paper','stone','scissors' not " + germer)

   elif(germer == "paper" and gamerBut == "paper"):
      print("you are in tiko " )

   elif(germer == "paper" and gamerBut == "stone"):
      print("you wine your paper and the comperter is stone")
      win += 1
  
   elif(germer == "paper" and gamerBut == "scissors"):
      print(" you lost you enter paper end the competer enter scissors")   
      lost += 1

   # enter stone 
   elif(germer ==  "stone" and gamerBut == "stone"):
    print("you in tiko")

   elif(germer ==  "stone" and gamerBut == "paper"):
      print("you in lose")
      lost+=1

   elif(germer ==  "stone" and gamerBut == "scissors"):
      print("you in win")
      win+=1   

   #enter scissors
   elif(germer ==  "scissors" and gamerBut == "scissors"):
      print("you in tiko")

   elif(germer ==  "scissors" and gamerBut == "stone"):
      print("you in lose")
      lost+=1

   elif(germer ==  "scissors" and gamerBut == "paper"):
      print("you in win")
      win+=1   
   print("how are you want to play ? enter exit ")
   x = input()
   if(x == "exit"):
      break
   