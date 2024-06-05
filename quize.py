# basic quize game in python

question = [[
    "which  programming language was first invented", "java", "php", "R",
    "python", 1
],
            [
                "which is the best progarming language for beginners",
                "python", "php", "R", "java", 1
            ],
            [
                "Who created Python?", "Guido van Rossum", "James Gosling",
                "Bjarne Stroustrup", "None", 1
            ],
            [
                " In which year was Python first released?", "1991", "1992",
                "1993", "1994", 1
            ],
            [
                "What does the term 'PEP' stand for in the Python community?",
                "Python Enchanment Proposal", "Python Environment Proposal",
                "Python Enhancer Proposal", "None", 1
            ]]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
i = 0
for i in range(0, len(question)):
  questions = question[i]
  print(f" Here is your Question for Rs.{levels[i]}")
  print("-------------------------------------------")
  print(f'{questions[i]}')
  print(
      f"a.{questions[1]}  b.{questions[2]} c.{questions[3]} d.{questions[4]}")
  reply = int(input("Enter your answer(1-4) or 0 to quit:\n"))
  if (reply == 1):
    print(f"Correct answer,you have won Rs.{levels[i]}")
    print("*********************************************")
  else:
    print("Wrong answer!")
    break
print(f"The total amount you have won is {levels[i - 1]}")
