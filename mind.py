import math, random, time
from datetime import datetime

coinTrue = 0
coinFalse = 0
coinSkip = 0
iterations = 0
numbers = 0

def mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers):
  if question > 0 and question < 101:
    start_time = datetime.now().replace(microsecond=0)
    while iterations < question:
      mathSign = random.randint(0, 2)
      a = math.floor((random.random()) * 10)
      b = math.floor((random.random()) * 10)
      numbers += 1

      if mathSign == 0:
        c = a + b
        answer = input("= "+ str(numbers) + ": " + str(a) + "+" + str(b) + "= ")
        if not answer:
          coinSkip += 1
          iterations += 1
          continue
        else:
          if math.fabs(int(answer)) == math.fabs(c):
            coinTrue += 1
          else:
            coinFalse += 1
            print("ОШИБКА")
      elif mathSign == 1:
        c = a - b
        answer = input("= "+ str(numbers) + ": " + str(a) + "-" + str(b) + "= ")
        if not answer:
          coinSkip += 1
          iterations += 1
          continue
        else:
          if math.fabs(int(answer)) == math.fabs(c):
            coinTrue += 1
          else:
            coinFalse += 1
            print("ОШИБКА")
      elif mathSign == 2:
        c = a * b
        answer = input("= "+ str(numbers) + ": " + str(a) + "*" + str(b) + "= ")
        if not answer:
          coinSkip += 1
          iterations += 1
          continue
        else:
          if math.fabs(int(answer)) == math.fabs(c):
            coinTrue += 1
          else:
            coinFalse += 1
            print("ОШИБКА")
      iterations += 1
    totalTime = ((datetime.now().replace(microsecond=0) - start_time))
    print("====== Количество верных упражнений: " + str(coinTrue))
    print("=== Количество НЕ верных упражнений: " + str(coinFalse))
    print("= Количество пропущенных упражнений: " + str(coinSkip))
    print("==== Время на выполнение упражнений: " + str(totalTime))
  else:
    print("=== КОЛИЧЕСТВО ЗАДАНИЙ НЕ ВЕРНО ===")


print("====================================")
name = input("=== Здравствуйте! Как вас зовут? ")
while True:
  try:
    question = int(input(str("=== " + name.title()) + ", cколько вы хотите выполнить заданий: "))
    mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers)
    print("====================================")
    repeatQuestion = input(str(name.title()) + ", хотите еще по упражняться?((да/д/y/yes)/ (нет/н/n/no)) ")
    if repeatQuestion == "да" or repeatQuestion == "д" or repeatQuestion == "y" or repeatQuestion == "yes":
      True
    else:
      break
  except ValueError:
    print("=== НЕВЕРНЫЙ ВВОД КОЛИЧЕСТВА ЗАДАНИЙ")

print("====================================")
