import math, random, time
from datetime import datetime
from logic import mathExercise

coinTrue = 0
coinFalse = 0
coinSkip = 0
iterations = 0
numbers = 0

print("====================================")
name = input("=== Здравствуйте! Как вас зовут? ")
while True:
  try:
    question = int(input(str("=== " + name.title()) + ", cколько вы хотите выполнить заданий: "))
    mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers, question)
    print("====================================")
    repeatQuestion = input(str(name.title()) + ", хотите еще по упражняться?((да/д/y/yes)/ (нет/н/n/no)) ")
    if repeatQuestion == "да" or repeatQuestion == "д" or repeatQuestion == "y" or repeatQuestion == "yes":
      True
    else:
      break
  except ValueError:
    print("=== НЕВЕРНЫЙ ВВОД КОЛИЧЕСТВА ЗАДАНИЙ")

print("====================================")
