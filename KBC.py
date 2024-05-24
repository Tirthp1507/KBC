questions= [
    [
        "What is the color of sky?","Blue","Red","Green","Yellow","none",1
    ],
    [
        "What is the color of sky in night?","Blue","Red","Black","Yellow","none",3
    ],
    [
        "What is the color of sun ?","Blue","Red","Black","Yellow","none",4
    ],
    [
        "What is the color of moon?","Blue","Red","Black","White","none",4
    ],
    [
        "How many are rings are there in symbol of Audi?","1","2","3","4","none",4
    ],
    [
        "How many players are there in football tam?","11","12","13","14","none",1
    ],
    [
        "Football is played by?","Bat","Ball","Racket","Golf stick","none",2
    ],
    [
        "Real Madrid is a club of which country?","Spain","Germany","Europe","Italy","none",1
    ],
    [
        "FC Barcelona is a club of which country?","Spain","Germany","Europe","Italy","none",1
    ],
    [
        "Borrusia Dortmund is a club of which country?","Spain","Germany","Europe","Italy","none",2
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  question =questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 
print(f"Your take home money is {levels[i]}")