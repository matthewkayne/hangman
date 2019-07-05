#Hangman

def hangman():

  import random

  words=["hello","matthew","table","rain","chair","mystery","liverpool","london","madrid","jeremy","computer","lesson","nice","well","great","awesome","brilliant"]
  stars=[]
  answer=[]
  rand_word=words[random.randint(0,len(words))]
  
  x="*"
  y=len(rand_word)

  print("The Word To Guess:",x * y)
  
  rand_word_answer = rand_word
  rand_word=list(rand_word)
  
  
  flag=False

  count=0

  stars=[]
  answer=[]
  
  for i in range(0,y):
    stars.append(x)
  
  
  while flag == False:

    guess=input("Guess a letter: ")

    if guess in rand_word:

      for i in[i for i,m in enumerate(rand_word) if m == guess]:
        

        answer.append(i)
      
        temp = rand_word[i]
        rand_word[i]=stars[i]
        stars[i] = temp

        temp_string=""
        for letters in range(len(stars)):
          temp_string+=stars[letters]
        

        if len(rand_word) == len(answer):
          print("Yes you got it right")
          flag=True
          
        else:
          pass
      print(temp_string)
            
    else:
      
      print("nope")
      count+=1
      print("You have", (5-count),"lives remaining")
      
      if count == 5:
        
        print("The word was",rand_word_answer)
        print("Game Over")
        flag=True
      
      else:
        
        pass     

hangman()