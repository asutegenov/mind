import math, random, time

from datetime import datetime
from logic import mathExercise

coinTrue = 0
coinFalse = 0
coinSkip = 0
iterations = 0
numbers = 0
exercise = 0

print("==============================================")
print("================== MIND v0.1 =================")
print("==============================================")

while True:
  try:

    print("==== 1. Упражнение 'Цепочка чисел' - Ур. 1 ===")
    print("==== 2. Таблица умножения  ===================")
    print("==== 3. Упражнение на сложение ===============") #Будущая цепочка чисел
    print("==== 4. Выход ================================")
    print("==============================================")

    num_question = int(input("========== Выберите пункт из списка: "))
    print("==============================================")

    if num_question == 1:
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers, 2)
    elif num_question == 2:
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers, 0)
    elif num_question == 3:
      mathExercise(iterations, coinTrue, coinFalse, coinSkip, numbers, 1)
    elif num_question == 4:
      print("================ See you later ===============")
      print("==============================================")
      break
    else:
      print("====== ВЫ ВВЕЛИ НЕВЕРНЫЙ НОМЕР ЗАДАНИЯ! ======")

    print("==============================================")

  except ValueError:

    print("==============================================")
    print("========= ВВЕДИТЕ, ПОЖАЛУЙСТА, ЦИФРЫ =========")
    print("==============================================")
